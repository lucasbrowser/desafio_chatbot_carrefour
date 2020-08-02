# Desafio TechChallenge ChatBot Banco Carrefour

Esse é um projeto para o desafio **TechChallenge do Banco Carrefour** através da Digital Inovation One. O desafio consiste em otimizar a comunicação entre os clientes e o Banco Carrefour.

A tecnologia aplicada no desenvolvimento foi através da linguagem de programação Python na versão 3.7.4 e conectado ao Telegram através de sua API, onde foi proposto a criação de um bot no Telegram para facilitar a comunicação com os clientes.

# Começando

Para executar o projeto será necessário instalar as seguintes bibliotecas **telepot** e **python-dotenv**:

Obs.: Para utilizar estas bibliotecas, é preciso ter o pip (gerênciador de pacotes do Python) instalado e configurado em sua máquina.

$ pip install telepot
$ pip install -U python-dotenv

E também será necessário obter a API do bot do Telegram.

# Iniciando

O projeto contém o arquivo carrefour.py que é responsável por rodar o script, onde temos a classe Chatbot.py que contém todas as instâncias do projeto e as falas do Chatbot estão armazenadas em um arquivo .json.

A API do Telegram por motivos de segurança está armazenada em um arquivo .env, que pode ser acessada através das variáveis de ambiente.