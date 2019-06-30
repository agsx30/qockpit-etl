# -*- coding: utf-8 -*-
import requests
import sys
import json
import configparser
from pprint import pprint
from dbLib import db_get_data

print('***** QOCKPIT | Teste *****')

# Verificação dos parâmetros de configuração.

config = configparser.ConfigParser()

config.read('setup.cfg')

if 'BASE_ENDPOINT' in config['API']:
  BASE_ENDPOINT = config['API']['BASE_ENDPOINT']
else:
  print('Endereço base não configurado => setup.cfg => [API] BASE_ENDPOINT=')
  sys.exit()

if 'DOMAIN' in config['API']:
  DOMAIN = config['API']['DOMAIN']
else:
  print('Domínio não configurado ({dominio}.qockpit.io) => setup.cfg => [API] DOMAIN=')
  sys.exit()

if 'API_TOKEN' in config['API']:
  API_TOKEN = config['API']['API_TOKEN']
else:
  print('Token da API não configurado => setup.cfg => [API] API_TOKEN=')
  sys.exit()

print("=> " + DOMAIN + ".qockpit.io")

# Verificação do acesso a API da plataforma.

print('Verificando API...')
r = requests.get(url = BASE_ENDPOINT + "/test") 
  
if ( r.status_code >= 400 ):
  print(r.content)
  sys.exit()

print("=======")

pprint(r.content)

print("=======")

# Validação do Token de Autenticação

print('Verificando autenticação...')
r = requests.get(url = BASE_ENDPOINT + "/test/token", 
  headers={ "X-API-DOMAIN": DOMAIN, "X-API-TOKEN": API_TOKEN }, 
  params = {})

if ( r.status_code >= 400 ):
  print(r.content)
  sys.exit()

print("=======")

pprint(r.content)

print("=======")

print('Testes concluídos.')
