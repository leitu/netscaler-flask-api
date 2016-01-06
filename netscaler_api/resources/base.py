import uuid
import logging
import json
from datetime import datetime
from flask_restful import Resource, reqparse, fields, marshal_with
import netscaler_api

LOGGER = logging.getLogger(__name__)

class Base(Resource):
  fields = {
      'task_id': fields.String,
  }
  decorators = [marshal_with(fields)]

  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('loadbalance', type=str, required=True)
    self.reqparse.add_argument('user', type=str, required=True)
    self.uuid = str(uuid.uuid4())
    super(Base, self).__init__()

  def persist_and_send(self, name, action, args):
    # convert from flask-ized object to dict for transport safety
    #args = dict(args)

    message = {
      'task_id': self.uuid,
      'status': 'init',
      'user': args.pop('user'),
      'creation_time': datetime.utcnow().isoformat(),
      'loadbalance': args.pop('loadbalance'),
      'action': action,
      'object': name,
      'arguments': json.dumps(args)
    }

    LOGGER.debug('sending to kvs and mq')
    netscaler_api.redis_store.hmset(self.uuid, message)
    message['arguments'] = args
    netscaler_api.queue.send_message(message)
    return message
