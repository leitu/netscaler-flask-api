import pika
import json
import logging
from urlparse import urlparse

logger = logging.getLogger(__name__)

class Queue(object):
  def __init__(self, url, **kwargs):
    self.queue = kwargs.get('queue', '')
    self.exchange = kwargs.get('exchange', '')
    self.key = kwargs.get('key', '')
    self.durable = kwargs.get('durable', True)
    self.url = url
    self.connection = None
    self.channel = None
    self.connect()

  def connect(self):
    result = urlparse(self.url)
    logger.info('Connecting to %s:%d', result.hostname, result.port)
    self.connection = pika.BlockingConnection(pika.URLParameters(self.url))
    self.channel = self.connection.channel()
    if self.exchange:
      self.channel.exchange_declare(
        exchange=self.exchange, durable=self.durable, type='topic'
      )
      self.channel.queue_declare(queue=self.queue, durable=self.durable)
      self.channel.queue_bind(exchange=self.exchange, queue=self.queue, routing_key=self.key)

  def send_message(self, payload, retry=False):
    message = json.dumps(payload)
    logger.debug('queue debugguer' + message)
    try:
      self.channel.basic_publish(
        exchange=self.exchange, routing_key=self.key, body=message,
        properties=pika.BasicProperties(
          content_type='application/json',
          delivery_mode=1
        )
      )
    except pika.exceptions.ConnectionClosed:
      logger.warning('Channel closed, reconnecting')
      self.connect()
      self.send_message(payload, True)

    if not retry:
      logger.info("Published to exchange '%s' with key '%s'",
        self.exchange, self.key
      )
      logger.debug('Message: %s', message)
