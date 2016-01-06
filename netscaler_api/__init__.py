from flask import Flask
from flask_restful import Api
from flask_redis import FlaskRedis
from netscaler_api.resources.task import Tasks, Task
from netscaler_api.resources.loadbalance import Loadbalances, Loadbalance, Appservers, Appserver, Services, Service
from netscaler_api.common.util import initialize_logging, construct_queue

initialize_logging('log-config.yaml')

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
api = Api(app, catch_all_404s=True)

redis_store = FlaskRedis(app, strict=True)
queue = construct_queue(app.config)

## Task Routes
api.add_resource(Tasks, '/v1/task/')
api.add_resource(Task, '/v1/task/<string:task_id>')

## Loadbalance Routes
api.add_resource(Loadbalances, '/v1/lb/')
api.add_resource(Loadbalance, '/v1/lb/<string:lbvserver>')

## Appserver Routes
api.add_resource(Appservers, '/v1/lb/as/')
api.add_resource(Appserver, '/v1/lb/as/<string:appserver>')

## Service Routes
api.add_resource(Services, '/v1/lb/ss/')
api.add_resource(Service, '/v1/lb/ss/<string:service>')
