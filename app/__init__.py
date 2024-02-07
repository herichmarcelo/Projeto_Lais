from flask import Flask

# Criação da instância do aplicativo Flask
app = Flask(__name__)

# Define a chave secreta
app.secret_key = 'sua_chave_secreta_aqui'  # Substitua 'sua_chave_secreta_aqui' por uma string única e secreta

# Importação das rotas
from app import routes