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
    BASE_ENDPOINT=https://qockpit.io/api
    DOMAIN=
    API_TOKEN=

A variável BASE_ENDPOINT deve ser mantida sem alteração.

A variável DOMAIN deve ser preenchida com o subdomínio do endereço utilizado para acessar a plataforma. Por exemplo, se o acesso é feito pelo endereço empresa.qockpit.io, deve-se preencher a variável DOMAIN da seguinte forma:

    DOMAIN=empresa

A variável API_TOKEN deve ser obtida na plataforma, no menu de configurações de integrações.

As configurações padrão de acesso ao banco de dados podem ser definidas localmente, também no arquivo setup.cfg.

    [FONTE]
    DBMS=
    HOST=
    USER=
    PASSWORD=
    DATABASE=

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
1. ODBC (Em construção)

## Requisitos

Necessário ter instalado na máquina o python e o driver python de conexão com a fonte de dados selecionada.

Normalmente, em MacOS e Linux, o python encontra-se instalado por padrão.

Para realizar a instalação do Python no Windows, acesse o link https://www.python.org/downloads/ para realizá-la.

### Componente para Conexão com o MSSQL

Para acesso ao Microsoft SQL Server, deve ser realizada a instalação do componente PYMSSQL.

Seguir as instruções de instalação do link: http://www.pymssql.org/en/stable/intro.html#install

### Componente para Conexão com o ORACLE

Para acesso ao ORACLE, deve ser realizada a instalação do componente cx_Oracle.

Seguir as instruções de instalação do link: https://cx-oracle.readthedocs.io/en/latest/installation.html

### Componente para Conexão com o ODBC

Em construção

## Instalação

Faça o download do arquivo: https://github.com/agsx30/qockpit-etl/archive/master.zip

Descompate os arquivos, e na pasta onde estão localizados os arquivos, realiza a configuração do arquivo setup.cfg e em seguida, realizar a execução do comando abaixo:

    python qockpit-teste.py

Se a execução ocorrer com sucesso, está pronto para programar as execuções de atualização como descrito no item "Serviços Disponíveis".

# Segurança

A utilização da API de integração do QOCKPIT apresenta uma estrutura segura devido as características abaixo:

1. Os parâmetros de conexão com o banco de dados são definidos localmente.
1. O código fonte do acesso ao banco de dados é aberto, podendo ser avaliado cada comando executado.
1. Os scripts executados são logados e exibidos na tela durante a execução.
1. A conexão com a plataforma é feita mediante token de autenticação gerado.


