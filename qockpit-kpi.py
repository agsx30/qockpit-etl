# -*- coding: utf-8 -*-
import requests
import sys
import json
import configparser
from pprint import pprint
from dbLib import db_get_data

print('***** QOCKPIT | Indicadores *****')

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

# Parâmetros de execução
# Primeiro padrâmetro deve ser o referência: Exemplo: 2019-01.
# Segundo parâmetro deve ser a frequência. Exemplo: m para mensal.

freq = "m"
ref = ""

if len(sys.argv) >= 2:
  ref = sys.argv[1]
  
if len(sys.argv) >= 3:
  freq = sys.argv[2]

# Busca das integrações cadastradas.

print('Verificando serviços registrados...')
r = requests.get(url = BASE_ENDPOINT + "/prepare/kpi", 
  headers={ "X-API-DOMAIN": DOMAIN, "X-API-TOKEN": API_TOKEN }, 
  params = {"freq": freq, "ref": ref})

if ( r.status_code >= 400 ):
  print(r.content)
  sys.exit()

print("=======")

pprint(json.loads(r.content))

print("=======")

# Execução das integrações cadastradas.

lista = json.loads(r.content)

for item in lista:
  if item['origem']['id'] > 0:
    print("[Buscando Indicador " + str( item['id'] ) + "...]")

    ret = db_get_data(item)
    
    params = { "id": item['id'], "ref": item['ref'], 
      "numerador": 0, "denominador": 1, "query": item['query']}

    if 'numerador' in ret.keys():
      params['numerador'] = ret['numerador'];
    else:
      print('Valor do numerador não retornado na query.')
      print("=======")
      continue

    if 'denominador' in ret.keys():
      params['denominador'] = ret['denominador'];

    pprint(params)

    print("[Enviando...]")
    
    r = requests.post(url = item['endpoint'], 
      headers={ "X-API-DOMAIN": DOMAIN, "X-API-TOKEN": API_TOKEN }, 
      params = params)
    print(r.content)

    print("=======")
    
print("***** Fim *****")