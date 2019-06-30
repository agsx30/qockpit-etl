import pymssql

class mssqlDb:

  def __init__(self, parms):
    self.host = parms['host']
    self.user = parms['user']
    self.password = parms['password']
    self.database = parms['database']

  def execute(self, query):

    connection = pymssql.connect(host = self.host, user = self.user, password = self.password, database = self.database)
    cursor = connection.cursor()

    cursor.execute(query)

    ret = {}

    """
    print(cursor.description)
    print(type(cursor.description).__name__)
    print(cursor.description[0][0])
    """

    for row in cursor:
      for idx, column in enumerate(row):
        ret[cursor.description[idx][0]] = column
      
    return ret