from flask import Flask
from flask import request
from flask_restful import Api
from flask_restful import Resource
from restfulhabilidades import ListarHabilidades
from restfulhabilidades import HabilidadesFuncoes
from restfulhabilidades import habilidades
import json


tarefas = [

    {"id": 0, "Responsavel": 'Felipe', "Atividade": 'Desenvolver Api Rest', "Status": 'Pendente',
     "Habilidades": ["Python", "Flask"]}

           ]


app = Flask(__name__)
api = Api(app)


class Tarefas(Resource):
    def get(self):
        return tarefas

    def post(self):
        habilidade_nao_cadastrada = False
        dados = json.loads(request.data)
        for habilidade in dados["Habilidades"]:
            if habilidade not in habilidades:
                habilidade_nao_cadastrada = True

        if habilidade_nao_cadastrada:
            return "Erro, você digitou alguma HABILIDADE que não está cadastrada! Tente novamente."
        else:
            posicao = len(tarefas)
            dados["id"] = posicao
            tarefas.append(dados)
            return f"Tarefa {dados} adicionada com sucesso!"


class TarefasMetodos(Resource):
    def get(self, id):
        return 'Não existe registro no banco de dados.' if len(tarefas) == 0 else tarefas[id]

    def put(self, id):
        status_modificado = False
        for tarefa in tarefas:
            if tarefa["id"] == id:
                status_modificado = True
                tarefa["Status"] = "Concluído"

        return f"Status modificado com sucesso: => {tarefa}" if status_modificado else "Tarefa não localizada!"

    def delete(self, id):
        tarefa_deletada = False
        tarefa_removida = ''
        for tarefa in tarefas:
            if tarefa["id"] == id:
                tarefa_deletada = True
                indice = tarefas.index(tarefa)
                tarefa_removida = tarefas.pop(indice)

        return f"Tarefa {tarefa_removida} deletada com sucesso!" if tarefa_deletada else "Tarefa não encontrada!"


api.add_resource(Tarefas, "/tarefas")
api.add_resource(TarefasMetodos, "/tarefas/<int:id>")
api.add_resource(ListarHabilidades, "/habilidades")
api.add_resource(HabilidadesFuncoes, "/habilidades/<int:id>")


app.run()
