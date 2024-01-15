from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

Base = declarative_base()
engine = create_engine("sqlite://")


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String, unique=True)
    endereco = Column(String)
    conta = relationship("Conta", back_populates='cliente')

    def __repr__(self):
        return (f"Cliente(Id = {self.id}, Nome = {self.nome}, Cpf = {self.cpf}, Endereço = {self.endereco},\n"
                f"Conta = {self.conta})")


class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(Integer)
    numero = Column(Integer)
    saldo = Column(Float)
    conta_id_cliente = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship("Cliente", back_populates='conta')

    def __repr__(self):
        return (f"\nConta(Id = {self.id}, Tipo = {self.tipo}, Agência = {self.agencia}, Saldo = {self.saldo} ,"
                f"Cliente ID = {self.conta_id_cliente})")


Base.metadata.create_all(engine)

with Session(bind=engine) as session:
    felipe = Cliente(nome='Felipe Rodrigues Fonseca', cpf='2387462', endereco='Rua Jardim Flores Nº 35 B. Centro',
                     conta=[Conta(tipo='Salário', agencia=33, numero=321432, saldo=0),
                            Conta(tipo='Corrente', agencia=33, numero=44455566, saldo=0)])
    luigi = Cliente(nome='Luigi Gomes Fonseca', cpf='13214232', endereco='Rua Gerenal Estíbal Nº4 B. Centro',
                     conta=[Conta(tipo='Salário', agencia=33, numero=233222245, saldo=0),
                            Conta(tipo='Corrente', agencia=33, numero=52333455, saldo=0)])
    session.add_all([felipe, luigi])
    session.commit()

# =-=-=-=-=-=-=-=-== Staments =-=-=-=-=-=-=-=-==
statement_where = select(Cliente).where(Cliente.nome.in_(['Luigi Gomes Fonseca']))
statement_where2 = select(Conta).where(Conta.conta_id_cliente.in_([2]))
statement_order_by = select(Cliente).order_by(Cliente.nome)
statement_join = select(Cliente.nome, Conta.tipo).join_from(Cliente, Conta)



# =-=-=-=-=-=-=-=-== Resultados e Prints =-=-=-=-=-=-=-=-==
ver_dados = lambda dados, sessao : sessao.execute(dados).fetchall()

resultado_statement_where = ver_dados(statement_where, session)
resultado_statement_where2 = ver_dados(statement_where2, session)
resultado_statement_order_by = ver_dados(statement_order_by, session)
resultado_statement_join = ver_dados(statement_join, session)


print('=-=-=-=-=-=-= Recuperando dados de um cliente específico =-=-=-=-=-=-=\n')
for nome in resultado_statement_where:
    print(nome)

print('\n=-=-=-=-=-=-= Recuperando contas bancárias de um ID de cliente específico =-=-=-=-=-=-=\n')
for conta in resultado_statement_where2:
    print(conta)

print('\n=-=-=-=-=-=-= Recuperando nomes de forma Ordenada =-=-=-=-=-=-=')
for nome in resultado_statement_order_by:
    print(f"\n{nome}")

print('\n=-=-=-=-=-=-= Recuperando os tipos de Conta Bancária que cada Cliente possui =-=-=-=-=-=-=\n')
for contas in resultado_statement_join:
    print(contas)
