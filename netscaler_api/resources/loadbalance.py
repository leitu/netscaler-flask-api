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
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    self.reqparse.add_argument('appservers', action='append', required=True)
    args = self.reqparse.parse_args()
    logger.info('Create lbvserver on %s', args['loadbalance'])
    self.persist_and_send('lbvserver', 'create', args)
    return {'task_id': self.uuid}, 202


class Loadbalance(Base):
  def get(self, lbvserver):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    args = self.reqparse.parse_args()
    args['lbvserver'] = lbvserver
    logger.info('Get info for loadbalance %s', lbvserver)
    self.persist_and_send('lbvserver', 'info', args)
    return {'task_id': self.uuid}, 202

  def delete(self, lbvserver):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    args = self.reqparse.parse_args()
    args['lbvserver'] = lbvserver
    logger.info('Delete %s', lbvserver)
    self.persist_and_send('lbvserver', 'delete', args)
    return {'task_id': self.uuid}, 202

  def put(self, lbvserver):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    self.reqparse.add_argument('status', required=True )
    args = self.reqparse.parse_args()
    args['lbvserver'] = lbvserver
    status = args['status']
    logger.info('%s %s', lbvserver, status)
    self.persist_and_send('lbvserver', 'update', args)
    return {'task_id': self.uuid}, 202

class Appservers(Base):
  def get(self):
     pass

  def post(self):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('appservers', action='append', required=True)
    args = self.reqparse.parse_args()
    logger.info('Create appserver on %s', args['loadbalance'])
    self.persist_and_send('appservers', 'create', args)
    return {'task_id': self.uuid}, 202

class Appserver(Base):
  def get(self):
     pass

  def delete(self, appserver):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    args = self.reqparse.parse_args()
    args['appserver'] = appserver
    logger.info('Delete %s', appserver)
    self.persist_and_send('appserver', 'delete', args)
    return {'task_id': self.uuid}, 202

  def put(self, appserver):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    self.reqparse.add_argument('status', required=True )
    args = self.reqparse.parse_args()
    args['appserver'] = appserver
    status = args['status']
    logger.info('%s %s', appserver, status)
    self.persist_and_send('appserver', 'update', args)
    return {'task_id': self.uuid}, 202

class Services(Base):
  def get(self):
     pass

  def post(self):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('appserver', action='append', required=True)
    args = self.reqparse.parse_args()
    logger.info('Create service on %s', args['loadbalance'])
    self.persist_and_send('service', 'create', args)
    return {'task_id': self.uuid}, 202

class Service(Base):
  def get(self):
     pass

  def delete(self, service):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    args = self.reqparse.parse_args()
    args['service'] = service
    logger.info('Delete %s', service)
    self.persist_and_send('service', 'delete', args)
    return {'task_id': self.uuid}, 202

  def put(self, service):
    self.reqparse.add_argument('loadbalance', type=str, required=True, location='json')
    self.reqparse.add_argument('user', required=True)
    self.reqparse.add_argument('vip', required=True)
    self.reqparse.add_argument('clientid', required=True )
    self.reqparse.add_argument('status', required=True )
    args = self.reqparse.parse_args()
    args['service'] = service
    status = args['status']
    logger.info('%s %s', service, status)
    self.persist_and_send('service', 'update', args)
    return {'task_id': self.uuid}, 202


