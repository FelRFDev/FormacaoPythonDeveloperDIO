from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import CheckConstraint



Base = declarative_base()
engine = create_engine("sqlite:///teste.db")
session = Session(bind=engine)


class Usuario(Base):
    __tablename__ = 'usuario'
    __table_args__ = (CheckConstraint('ativo In (0,1)', name='check_ativo_0,1'),)
    id = Column(Integer, autoincrement=True, primary_key=True)
    login = Column(String, unique=True)
    senha = Column(String, unique=True)
    ativo = Column(Integer)

    def cadastrar_usuario(self):
        session.add(self)
        session.commit()

    def remover_usuario(self):
        session.delete(self)
        session.commit()


class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    idade = Column(Integer)

    def salvar(self):
        session.add(self)
        session.commit()

    def deletar(self):
        session.delete(self)
        session.commit()


Base.metadata.create_all(engine)

usuario1 = Usuario(login='Darcio', senha=1111, ativo=0)
usuario2 = Usuario(login='Valeria', senha=3333, ativo=1)

usuario1.cadastrar_usuario()
usuario2.cadastrar_usuario()
