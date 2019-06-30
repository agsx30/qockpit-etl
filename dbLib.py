from q_mssql import mssqlDb

def db_get_data (item):
  query = item['query']

  x = mssqlDb(item['origem']['parms'])
  
  return x.execute(query)

  