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
    x = mssqlDb(item['origem']['parms'])
  
  return x.execute(query)

def check_config (parser, var, item):
  if var in parser['FONTE']:
  	info = parser['FONTE'][var]
  	if info:
  	  item['origem']['parms'][var] = info


  