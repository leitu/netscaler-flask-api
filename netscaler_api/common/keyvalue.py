import redis

class KeyValue():
  def __init__(self, host, port, db):
    self.host = host
    self.port = port
    self.db = db
    self.kv = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

  def host(self, *newhost):
    if newhost:
      self.host = newhost
      self.kv = redis.StrictRedis(host=self.host, port=self.port, db=self.db)
    self.host

  def port(self, *newport):
    if newport:
      self.port = newport
      self.kv = redis.StrictRedis(host=self.host, port=self.port, db=self.db)
    self.port

  def db(self, *newdb):
    if newdb:
      self.db = newdb
      self.kv = redis.StrictRedis(host=self.host, port=self.port, db=self.db)
    self.db

  def get(self, key):
    return self.kv.get(key)

  def set(self, key, value):
    return self.kv.set(key, value)

  def expire(self, key, time):
    return self.kv.expire(key, time)
