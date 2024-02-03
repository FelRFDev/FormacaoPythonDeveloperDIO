from flask import Flask
from flask_restful import Resource
from flask import request
from flask_restful import Api
from Aula_Flask.ormpratica import Funcionarios, session, Usuario
from flask_httpauth import HTTPBasicAuth


autenticador = HTTPBasicAuth()


@autenticador.verify_password
def verificador(login, senha):
    if not (login, senha):
        return False
    credenciais_corretas = session.query(Usuario).filter_by(login=login, senha=senha).first()
    if credenciais_corretas != None:
        usuario = session.query(Usuario).filter_by(login=login).first()
        return True if usuario.ativo == 1 else False
    else:
        return False



app = Flask(__name__)
api = Api(app)


class Funcionario(Resource):
    def get(self, nome):
        funcionarios_lista = session.query(Funcionarios).filter_by(nome=nome).first()
        response = {
            "id": funcionarios_lista.id,
            "nome": funcionarios_lista.nome,
            "idade": funcionarios_lista.idade
        }

        return response

    @autenticador.login_required
    def put(self, nome):
        funcionarios_lista = session.query(Funcionarios).filter_by(nome=nome).first()
        novos_dados = request.json
        if "nome" in novos_dados:
            funcionarios_lista.nome = novos_dados["nome"]
        if "idade" in novos_dados:
            funcionarios_lista.idade = novos_dados["idade"]

        funcionarios_lista.salvar()
        response = {
            "id":funcionarios_lista.id,
            "nome": funcionarios_lista.nome,
            "idade": funcionarios_lista.idade
                    }
        return response

    @autenticador.login_required
    def delete(self, nome):
        funcionarios_lista = session.query(Funcionarios).filter_by(nome=nome).first()
        msg_retorno = f"Funcionario: {funcionarios_lista.nome} deletado com sucesso!"
        funcionarios_lista.deletar()
        return msg_retorno

class Funcionario2(Resource):
    def get(self):
        funcionarios = session.query(Funcionarios).all()
        lista_de_funcionarios = [{"id":funcionario.id, "nome":funcionario.nome, "idade": funcionario.idade}
                                 for funcionario in funcionarios]
        return lista_de_funcionarios

    @autenticador.login_required
    def post(self):
        novo_funcionario = request.json
        cadastrar_novo_funcionario = Funcionarios(nome=novo_funcionario["nome"], idade=novo_funcionario["idade"])
        cadastrar_novo_funcionario.salvar()
        return f"Funcionário: {cadastrar_novo_funcionario.nome} cadastrado com sucesso!"

api.add_resource(Funcionario, "/consulta/<string:nome>")
api.add_resource(Funcionario2, "/manipular")

app.run()
