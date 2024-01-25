from flask_restful import Resource
from flask import request
import json

habilidades = [
    "Python", "Django", "Flask", "Postman", "Sql", "NoSql",
    "Pandas", "Matplotlib", "OpenCV"
]


class ListarHabilidades(Resource):
    def get(self):
        return habilidades

    def post(self):
        nova_habilidade = json.loads(request.data)
        habilidades.append(nova_habilidade)
        return f"A habilidade '{nova_habilidade}' foi adicionada com sucesso!"


class HabilidadesFuncoes(Resource):
    def put(self, id):
        novo_nome = json.loads(request.data)
        habilidades[id] = novo_nome
        return f"A habilidade {novo_nome} foi acrescentada com sucesso!"

    def delete(self, id):
        habilidades.pop(id)
        return "Habilidade removida com sucess
