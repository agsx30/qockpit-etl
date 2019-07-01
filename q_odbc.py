import pyodbc

class odbcDb:

  def __init__(self, parms):
    self.host = parms['host']
    self.user = parms['user']
    self.password = parms['password']
    self.database = parms['database']

  def execute(self, query):
    return pyodbc.connect("DSN=" + self.host + ";UID=" + self.user + ";PWD=" + self.password)
