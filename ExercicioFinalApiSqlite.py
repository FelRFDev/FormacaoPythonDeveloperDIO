
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session



Base = declarative_base()
engine = create_engine("sqlite:///funcionarios.db")
session = Session(engine)



class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    senha = Column(Integer)
    status = Column(String)
    def salvar(self):
        session.add(self)
        session.commit()


class Funcionario(Base):
    __tablename__ = 'funcionario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)
    contato = Column(String, unique=True)
    cargo = Column(String)
    def salvar(self):
        session.add(self)
        session.commit()

    def remover(self):
        session.delete(self)
        session.commit()


Base.metadata.create_all(engine)

admin = Usuario(login='admin', senha=123, status='ADM')
usuario1 = Usuario(login='user1', senha=321, status='usuario')

admin.salvar()
usuario1.salvar()


felipe = Funcionario(nome='Felipe Rodrigues Fonseca', contato="email.com", cargo="Dev.Backend")
gabriel = Funcionario(nome='Gabriel Rodrigues Fonseca', contato="algummail.com", cargo="Dev.Frontend")

felipe.salvar()
gabriel.salvar()
