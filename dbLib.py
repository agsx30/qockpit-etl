from q_mssql import mssqlDb
import configparser
import sys

def db_get_data (item):

  query = item['query']

  config = configparser.ConfigParser()
  config.read('setup.cfg')

  check_config (config, 'dbms', item)
  check_config (config, 'host', item)
  check_config (config, 'user', item)
  check_config (config, 'password', item)
  check_config (config, 'database', item)

  if item['origem']['parms']['dbms'] == 'mssql':
    driver = mssqlDb(item['origem']['parms'])

  conn = driver.connect()
  cursor = conn.cursor()
  cursor.execute(query)

  ret = {}

  for row in cursor:
    for idx, column in enumerate(row):
      ret[cursor.description[idx][0]] = column
    
  return ret

def check_config (parser, var, item):
  if var in parser['FONTE']:
    info = parser['FONTE'][var]
    if info:
  	  item['origem']['parms'][var] = info


  