import logging
import json
from datetime import timedelta, datetime
from flask_restful import Resource, abort
import netscaler_api

logger = logging.getLogger(__name__)

class Tasks(Resource):
  def get(self):
    logger.info('Get list of tasks')
    keys = ('task_id', 'creation_time', 'status', 'user')
    tasks = []
    for task_id in netscaler_api.redis_store.keys('*'):
      vals = netscaler_api.redis_store.hmget(task_id, keys)
      task = dict(zip(keys, vals))
      tasks.append(task)
    return tasks, 200


class Task(Resource):
  def get(self, task_id):
    logger.info('Get task status')
    task_status = netscaler_api.redis_store.hgetall(task_id)

    if task_status['status'] == 'init':
      self.__expire(task_status)

    if task_status.get('arguments'):
      task_status['arguments'] = json.loads(task_status['arguments'])

    if task_status:
      return task_status, 200
    else:
      abort(404, message="No such task '{}'".format(task_id))

  def __expire(self, task):
    lifetime = netscaler_api.app.config['TASK_LIFETIME_SECONDS']
    if self.__check_expire(task['creation_time'], lifetime):
      logger.warning("Task '%s' has expired", task['task_id'])
      task['status'] = 'expired'
      task['reason'] = 'Task expired during processing'
      netscaler_api.redis_store.hmset(task['task_id'], task)

  @staticmethod
  def __check_expire(timestamp, maximum):
    now = datetime.utcnow()
    then = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
    diff = now - then
    if diff.total_seconds() > maximum:
      return True
    return False
