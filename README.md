# netscaler-flask-api
use flask to get post netscaler

##Pre requirment
   * RabbitMQ
   * Flask
   * Python
   
```
mkdir web;cd web
virtualenv flask
source flask/bin/activate
pip install flask
pip install flask_restful
```

##setup flask environment
~~~
python app.py
~~~
The host will run at http://localhost:5000

~~~
curl -H "Content-Type: application/json" -X POST -d '{ "loadbalance": "192.168.1.1","vip": "10.10.10.1", \
        "clientid": "test", "appservers": ["10.10.10.2","10.10.10.3"]}' http://localhost:5000/v1/lb/
~~~
You will check the data will be transfer to rabbitmq

~~~
{
  "status": "init",
  "object": "lbvserver", 
  "user": "foo", 
  "task_id": "578e751b-f04a-41eb-8c15-f198e29af6ec", 
  "action": "create", 
  "loadbalance": "192.168.1.1", 
  "creation_time": "2015-12-30T08:05:31.801067", 
  "arguments": {"appservers": ["10.10.10.2", "10.10.10.3"], "vip": "10.10.10.1", "clientid": "test"}
}
~~~
