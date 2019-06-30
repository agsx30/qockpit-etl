# QOCKPIT: Integração

## Introdução

Script em Python para execução da API de integração do QOCKPIT.

Inicialmente, deve-se realizar o cadastro das integrações desejadas na plataforma. Com a execução desse script serão executados os seguintes passos:

1. Consultar a plataforma QOCKPIT. 
1. identificar os scripts que precisam ser executados.
1. Acessar as fontes de dados indicadas para cada integração, e obter os respectivos dados.
1. Enviar o resultado obtido para a plataforma.

## Configurações

Devem ser realizadas as configurações abaixo no arquvio setup.cfg.

    [API]
    BASE_ENDPOINT=http://qockpit.io/api
    DOMAIN=
    API_TOKEN=

A variável BASE_ENDPOINT deve ser mantida sem alteração.

A variável DOMAIN deve ser preenchida com o subdomínio do endereço utilizado para acessar a plataforma. Por exemplo, se o acesso é feito pelo endereço empresa.qockpit.io, deve-se preencher a variável DOMAIN da seguinte forma:

    DOMAIN=empresa

A variável API_TOKEN deve ser obtida na plataforma, no menu de configurações de integrações.

## Serviços Disponíveis 

### Integração de Indicadores

Para realizar a integrações de indicadores, deve ser executado o script abaixo:

Para realizar a integração dos indicadores de um mês específico:

    python qockpit-kpi.py 2019-01

Para realizar a integração dos indicadores de do mês anterior:

    python qockpit-kpi.py MA

## Fontes de Dados disponíveis

1. Microsoft SQL Server
1. ORACLE (Em construção)
1. JDBC (Em construção)

## Requisitos

Necessário ter instalado na máquina o python e o driver python de conexão com a fonte de dados selecionada.

Normalmente, em MacOS e Linux, o python encontra-se instalado por padrão.

Para realizar a instalação do Python no Windows, acesse o link https://www.python.org/downloads/ para realizá-la.

## Instalação

Faça o download do arquivo: https://github.com/agsx30/qockpit-etl/archive/master.zip

Descompate os arquivos, e na basta onde estão localizados os arquivos, realiza a configuração do arquivo setup.cfg e em seguinte pode realizar a execução do comando abaixo:

    python qockpit-teste.py

Se a execução ocorrer com sucesso, pode programar as execuções de atualização como descrito no item "Serviços Disponíveis".


