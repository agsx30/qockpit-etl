import pymssql

class mssqlDb:

  def __init__(self, parms):
    self.host = parms['host']
    self.user = parms['user']
    self.password = parms['password']
    self.database = parms['database']

  def connect(self):
    return pymssql.connect(host = self.host, user = self.user, password = self.password, database = self.database)
