from flask import Flask
from flask import jsonify
from flask import request
import json


tarefas = [

           ]

app = Flask(__name__)


@app.route("/obter_tarefa", methods=["GET"])
def obter_tarefas():
    if len(tarefas) == 0:
        return 'Não existe registro no banco de dados.'
    else:
        return jsonify(tarefas)


@app.route('/obter_tarefa_id/<int:id>', methods=["GET"])
def ober_tarefa_id(id):
    if len(tarefas) == 0:
        return 'Não existe registro no banco de dados.'
    else:
        return jsonify(tarefas[id])


@app.route('/remover_tarefa/<int:id>', methods=["DELETE"])
def remove_tarefa(id):
    for tarefa in tarefas:
        if tarefa["Id"] == id:
            tarefas.pop(tarefas.index(tarefa))
    return "Tarefa Removida"


@app.route('/adicionar_tarefa', methods=["POST"])
def adicionar_tarefa():
    nova_tarefa = json.loads(request.data)
    tarefas.append(nova_tarefa)
    nova_tarefa_id = tarefas.index(nova_tarefa)
    tarefas[nova_tarefa_id]["Id"] = nova_tarefa_id
    return 'Tarefa Adicionada com Sucesso!'



@app.route('/modificar_status/<int:id>', methods=["PUT"])
def modificar_status(id):
    for tarefa in tarefas:
        if tarefa["Id"] == id:
            tarefa["Status"] = "Concluído"

    return "Status alterado com sucesso!"


app.run()
