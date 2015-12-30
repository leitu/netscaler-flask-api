# Flask and Flask-RESTful variables
DEBUG=False
ERROR_404_HELP=False
BUNDLE_ERRORS=True
# General applicatino variables
TASK_LIFETIME_SECONDS=900
# Redis settings
REDIS_URL='redis://localhost:6379'
# Pika settings
QUEUE_USERNAME='test'
QUEUE_PASSWORD='test'
QUEUE_HOSTNAME='localhost'
QUEUE_PORT=5672
QUEUE_VHOST='%2F'
QUEUE_EXCHANGE='loadbalance'
QUEUE_QUEUE='loadbalance'
QUEUE_ROUTING_KEY='loadbalance'
QUEUE_DURABILITY=True
