import re
import yaml
import logging
import logging.config
from queue import Queue

def initialize_logging(config_file):
  config = yaml.load(open(config_file, 'r'))
  logging.config.dictConfig(config)

def construct_queue(config):
  url = 'amqp://{0}:{1}@{2}:{3}/{4}'.format(
    config.get('QUEUE_USERNAME'),
    config.get('QUEUE_PASSWORD'),
    config.get('QUEUE_HOSTNAME'),
    config.get('QUEUE_PORT'),
    config.get('QUEUE_VHOST')
  )
  return Queue(url,
    exchange=config.get('QUEUE_EXCHANGE'),
    durable=config.get('QUEUE_DURABILITY'),
    key=config.get('QUEUE_ROUTING_KEY'),
    queue=config.get('QUEUE_QUEUE')
  )
