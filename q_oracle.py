import cx_Oracle

class oracleDb:

  def __init__(self, parms):
    self.host = parms['host']
    self.user = parms['user']
    self.password = parms['password']
    self.database = parms['database']

  def execute(self):
  	parms = self.user + "/" + self.password + "@" + self.host + "/" + self.database
    return cx_Oracle.connect(parms)
    