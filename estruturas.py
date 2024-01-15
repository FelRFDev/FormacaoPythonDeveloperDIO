from abc import ABC, abstractmethod
import datetime

class Transacao(ABC):
    @abstractmethod
    def deposito(self):
        pass
 
    @abstractmethod
    def saque(self):
        pass
 
 
class Pessoa_Fisica:
    def __init__(self, nome: str, cpf: int, dt_nascimento: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = dt_nascimento

    def __str__(self):
        return f'Class: {self.__class__.__name__} / Att: {"".join([f"{key} : {value} " for key,value in self.__dict__.items()])}'

    @property
    def nome(self):
        return self.__nome


class Pessoa_Juridica:
    def __init__(self, nome: str, cnpj: int, dt_nascimento: str ):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__data_nascimento = dt_nascimento

    def __str__(self):
        return f'Class: {self.__class__.__name__} / Att: {"".join([f"{key} : {value} " for key,value in self.__dict__.items()])}'

    @property
    def nome(self):
        return self.__nome
 
# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
 
class Cliente:
    def __init__(self, endereco: str):
        self.__endereco = endereco
        self.__contas = list()
        self.__classificacao = '' # vai receber as classes pessoa fisica ou juridica

    def __str__(self):
        return f'Class: {__class__.__name__} / Att: {"".join([f"{key} : {value} " for key, value in self.__dict__.items()])}'

    @property
    def contas(self):
        return self.__contas

    @property
    def classificacao(self):
        return self.__classificacao
    
    @classificacao.setter
    def classificacao(self, dados):
        self.__classificacao = dados
    
    def adicionar_conta(self, conta):
        self.__contas.append(conta)
 
    def realizar_transacao(self, numero, senha, transacao):
        for conta in self.__contas:
            if conta.__numero == numero and conta.__senha == senha:
                match transacao:
                    case 'saque':
                        conta.__sacar()
                    case 'deposito':
                        conta.__depositar()
        
 
 
# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
 
class Conta:
    def __init__(self, cliente, senha: int, numero: int,  agencia ='00055', saldo=0):
        self.__numero = numero
        self.__agencia = agencia
        self.__saldo = saldo
        self.__cliente = cliente #recebe a classe Cliente
        self.__historico = Historico() #recebe a classe Historico
        self.__senha = senha

    @property
    def historico(self):
        return self.__historico


    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def senha(self):
        return self.__senha

    def exibe_saldo_tela(self):
        saldo = self.__ver_saldo()
        return saldo

    def __ver_saldo(self):
        return self.__saldo

    def realizar_deposito(self, dados_digitados_validos, valor):
        match dados_digitados_validos:
            case True:
                self.__depositar(valor)
            case False:
                pass

    def realizar_saque(self, dados_digitados_validos, valor):
        match dados_digitados_validos:
            case True:
                self.__sacar(valor)
            case False:
                pass


    def __depositar(self, valor: float) -> bool:
        total = self.__saldo + valor
        if total < self._limite and valor != 0 or total == self._limite and valor != 0:
            self.__saldo += valor
            self.__historico.adicionar_transacao(Transacao_Bancaria.deposito(valor))
            print(self.__historico.registros)


    def __sacar(self, valor: float) -> bool:
        if valor <= self.__saldo and valor != 0:
            self.__saldo -= valor
            self.__historico.adicionar_transacao(Transacao_Bancaria.saque(valor))






# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
class Conta_Corrente(Conta):
    def __init__(self, limite = 15000.0, **kwargs):
        super().__init__(**kwargs)
        self._limite = limite
        self._limite_de_saque = 3
        self._saques_realizados = 0


    def __str__(self):
        return f'Class: {self.__class__.__name__} / Att: {"".join([f"{key} : {value} " for key,value in self.__dict__.items()])}'

    @property
    def limite_de_saque(self):
        return self._limite_de_saque

    @property
    def saques_realizados(self):
        return self._saques_realizados

    def contabilizar_saque(self):
        self._saques_realizados +=1

    @classmethod
    def gerar_conta(cls, **kwargs):
        return cls(**kwargs)
    
# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
 
class Transacao_Bancaria(Transacao):
    def __init__(self, transacao_realizada):
        self.transacao_realizada = transacao_realizada

    @classmethod
    def deposito(cls, valor):
        return cls({'Tipo de Transação': 'Depósito', 'Valor Depositado': f'R$ {valor}', 'Data da Transação':
            f'{datetime.datetime.now().strftime("Data: %d/%m/%Y | Hora: %H:%M")}'})
    
    @classmethod
    def saque(cls, valor):
        return cls({'Tipo de Transação': 'Saque', 'Valor do Saque': f'R$ {valor}',
                                   'Data da Transação':
                                       f'{datetime.datetime.now().strftime("Data: %d/%m/%Y | Hora: %H:%M")}'})
    def __str__(self):
        return f'Class: {self.__class__.__name__} / Att: {"".join([f"{key} : {value} " for key,value in self.__dict__.items()])}'

 
class Historico:
    def __init__(self):
        self.registros = [] # vai receber a classe Transacao_Bancaria
    
    def adicionar_transacao(self, transacao):
        self.registros.append(transacao)

