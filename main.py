# Instalação dos pacotes necessários no Colab
!pip install flask
!pip install flask-ngrok

# Importações
from flask import Flask
from flask_ngrok import run_with_ngrok

funcionarios = [
    {"Nome": "Felipe", "Idade": 35, "Cargo": "Dev. Back End"},
    {"Nome": "Gabriel", "Idade": 27, "Cargo": "Dev. Front End"},
    {"Nome": "Darcio", "Idade": 60, "Cargo": "Analista de Dados"},
]



app = Flask(__name__)


@app.route("/funcionario/<int:id>", methods=["GET"])
def funcionario(id):
    try:
      funcionario = funcionarios[id]
    except IndexError:
      return "ID inválido! Tente novamente."
    else:
      return funcionario


@app.route("/funcionario_nome/<string:nome>", methods=["GET"])
def funcionario_nome(nome):
    funcionario_localizado = False
    funcionario = ''
    for funcionario_cadastrado in funcionarios:
        if funcionario_cadastrado["Nome"] == nome:
            funcionario_localizado = True
            posicao = funcionarios.index(funcionario_cadastrado)
            funcionario = funcionarios[posicao]

    return funcionario if funcionario_localizado else "Nome inválido, funcionário não localizado!"


@app.route("/total_de_registros", methods=["GET"])
def total_de_registros():
    return f"Total de funcionários cadastrados: [{len(funcionarios)}]"
    
    
run_with_ngrok(app)
app.run()
