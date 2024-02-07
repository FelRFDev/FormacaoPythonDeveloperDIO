from flask import Flask
from flask_restful import Resource
from flask import request
from flask_restful import Api
from Aula_Flask.ormpratica import Funcionario, session, Usuario
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
api = Api(app)
autenticador = HTTPBasicAuth()



@autenticador.verify_password
def valida_usuario(login, senha):
    if not (login, senha):
        return False
    try:
        busca_usuario = session.query(Usuario).filter_by(login=login).first()
    except Exception:
        return False
    else:
        if busca_usuario.status != 'ADM':
            return False
        return busca_usuario.senha == int(senha)


class ManipularFuncionarios(Resource):
    def get(self):
        funcionarios_cadastrados = session.query(Funcionario).all()
        response = [{
            "Nome": funcionario.nome,
            "Contato": funcionario.contato,
            "Cargo": funcionario.cargo
        } for funcionario in funcionarios_cadastrados]
        return response


    @autenticador.login_required
    def post(self):
        response = request.json
        novo_cadastro = Funcionario(nome=response["nome"], contato=response["contato"], cargo=response["cargo"])
        novo_cadastro.salvar()
        return f"Usuário {response['nome']} cadastrado com sucesso!"


class ConsultarFuncionario(Resource):
    def get(self, nome):
        funcionarios_lista = session.query(Funcionario).filter_by(nome=nome).first()
        try:
            response = {
                "nome": funcionarios_lista.nome,
                "contato": funcionarios_lista.contato,
                "cargo": funcionarios_lista.cargo}
        except AttributeError:
            return "Funcionario Nao Encontrado"
        else:
            return response


    @autenticador.login_required()
    def put(self, nome):
        busca_cliente = session.query(Funcionario).filter_by(nome=nome).first()
        try:
            novos_dados = request.json
            if not novos_dados:
                raise ValueError
        except ValueError:
            return "Informe os novos dados"
        else:
            try:
                busca_cliente.nome = novos_dados["nome"]
                busca_cliente.contato = novos_dados["contato"]
                busca_cliente.cargo = novos_dados["cargo"]
            except AttributeError:
                return "Funcionario não encontrado"
            else:
                busca_cliente.salvar()
                return f"Alterações feitas com sucesso para: {novos_dados}"

    @autenticador.login_required()
    def delete(self, nome):
        busca_funcionario = session.query(Funcionario).filter_by(nome=nome).first()
        try:
            busca_funcionario.remover()
        except:
            return 'Funcionário não encontrado!'
        else:
            return f"Usuário {busca_funcionario.nome} removido com sucesso!"




api.add_resource(ManipularFuncionarios, "/funcionarios")
api.add_resource(ConsultarFuncionario, "/consulta/<string:nome>")

if __name__ == "__main__":
    app.run()
