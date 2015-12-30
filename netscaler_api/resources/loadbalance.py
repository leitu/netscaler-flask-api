import logging
from flask_restful import abort
from netscaler_api.resources.base import Base

logger = logging.getLogger(__name__)

class Loadbalances(Base):
  def get(self):
    args = self.reqparse.parse_args()
    logger.info('List Loadbalances')
    self.persist_and_send('loadbalance', 'list', args)
    return {'task_id': self.uuid}, 202

  def post(self):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    #self.reqparse.add_argument('appservers', type=str, required=True, location='json')
    #self.reqparse.add_argument('clientid', type=str, required=True, location='json')
    #self.reqparse.add_argument('vip', type=str, required=True, location='json')
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    self.reqparse.add_argument('appservers', action='append', required=True)
    args = self.reqparse.parse_args()
    logger.info('Create loadbalance on %s', args['loadbalance'])
    self.persist_and_send('lbvserver', 'create', args)
    return {'task_id': self.uuid}, 202


class Loadbalance(Base):
  def get(self, loadbalance):
    args = self.reqparse.parse_args()
    args['loadbalance'] = loadbalance
    logger.info('Get info for loadbalance %s', args['loadbalance'])
    self.persist_and_send('loadbalance', 'info', args)
    return {'task_id': self.uuid}, 202

  def delete(self, loadbalance):
    args = self.reqparse.parse_args()
    args['loadbalance'] = loadbalance
    logger.info('Delete loadbalance %s', args['loadbalance'])
    self.persist_and_send('loadbalance', 'destroy', args)
    return {'task_id': self.uuid}, 202


