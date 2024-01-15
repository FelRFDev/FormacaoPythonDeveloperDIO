from estruturas import *
import customtkinter as ctk
import base64
import tkinter as tk
from b64imagens import *
from tkinter import messagebox
from random import randint


clientes_pf = list()
clientes_pj = list()

class Janela_Saque:
    """
    Classe que contém toda a estrutura para realizar o procedimento de Saque!
    Contém, botões, entrys, e funcções de validação.
    """
    def sacar(self):
        self.janela_sacar = ctk.CTkToplevel()
        self.janela_sacar.title('BRASBANK - Janela Saque')
        self.janela_sacar.resizable(False, False)
        self.janela_sacar.geometry('700x720+650+100')
        self.widgets_saque()
        self.janela_sacar.grab_set()
        self.janela_sacar.focus_force()
        self.janela_sacar.mainloop()

    def widgets_saque(self):
        # =-=-=-=-=-=-=-=-= Criando Bordas e Cabeçalho ==-=-=-=-=-=-=-=-=-=-=-=-
        self.borda_saque = ctk.CTkFrame(master=self.janela_sacar, width=700, height=720, fg_color='#708090')
        self.borda_saque.place(x=0, y=0)

        self.segunda_tela_saque = ctk.CTkFrame(master=self.janela_sacar, width=500, height=500,
                                                  fg_color="#8FBC8F",
                                                  bg_color='#708090')
        self.segunda_tela_saque.place(x=110, y=140)

        self.cabecalho_saque = ctk.CTkLabel(master=self.janela_sacar, text='REALIZAR SAQUE',
                                               font=('Impact', 20))
        self.cabecalho_saque.place(x=310, y=130)

        # =-=-=-=-=-=-=-=-= Criando Paineis de Texto ==-=-=-=-=-=-=-=-=-=-=-=-
        self.painel_nome_saque = ctk.CTkFrame(master=self.janela_sacar, width=98, height=28, fg_color='#708090',
                                                 bg_color="#8FBC8F")
        self.painel_conta_saque = ctk.CTkFrame(master=self.janela_sacar, width=98, height=28, fg_color='#708090',
                                                  bg_color="#8FBC8F")
        self.painel_senha_saque = ctk.CTkFrame(master=self.janela_sacar, width=98, height=28, fg_color='#708090',
                                                  bg_color="#8FBC8F")
        self.painel_valor_saque = ctk.CTkFrame(master=self.janela_sacar, width=98, height=28, fg_color='#708090',
                                                  bg_color="#8FBC8F")

        self.nome_texto_saque = ctk.CTkLabel(master=self.janela_sacar, text='Nome', bg_color='#708090',
                                                font=('Impact', 14), text_color='#E0FFFF')
        self.conta_texto_saque = ctk.CTkLabel(master=self.janela_sacar, text='Conta', bg_color='#708090',
                                                 font=('Impact', 14), text_color='#E0FFFF')
        self.senha_texto_saque = ctk.CTkLabel(master=self.janela_sacar, text='Senha', bg_color='#708090',
                                                 font=('Impact', 14), text_color='#E0FFFF')
        self.valor_texto_saque = ctk.CTkLabel(master=self.janela_sacar, text='Valor R$', bg_color='#708090',
                                                 font=('Impact', 14), text_color='#E0FFFF')

        # =-=-=-=-=-=-=-=-= Places ==-=-=-=-=-=-=-=-=-=-=-=-
        self.painel_nome_saque.place(x=200, y=200)
        self.painel_conta_saque.place(x=200, y=280)
        self.painel_senha_saque.place(x=200, y=360)
        self.painel_valor_saque.place(x=200, y=440)

        self.nome_texto_saque.place(x=220, y=200)
        self.conta_texto_saque.place(x=220, y=280)
        self.senha_texto_saque.place(x=220, y=360)
        self.valor_texto_saque.place(x=220, y=440)

        # =-=-=-=-=-=-=-=-= Criando Widgets para Depósito ==-=-=-=-=-=-=-=-=-=-=-=-
        self.nome_saque_entry = ctk.CTkEntry(master=self.janela_sacar, width=300, bg_color="#8FBC8F")
        self.conta_saque_entry = ctk.CTkEntry(master=self.janela_sacar, width=300, bg_color="#8FBC8F")
        self.senha_saque_entry = ctk.CTkEntry(master=self.janela_sacar, width=300, bg_color="#8FBC8F")
        self.valor_saque_entry = ctk.CTkEntry(master=self.janela_sacar, width=300, bg_color="#8FBC8F")
        self.check_box_PessoaFisica = ctk.CTkCheckBox(master=self.janela_sacar, text='Pessoa Física',
                                                      bg_color="#8FBC8F")
        self.check_box_PessoaJuridica = ctk.CTkCheckBox(master=self.janela_sacar, text='Pessoa Jurídica',
                                                        bg_color="#8FBC8F")
        self.botão_saque = ctk.CTkButton(master=self.janela_sacar, text='Realizar Saque',
                                                     bg_color="#8FBC8F", command=self.realizar_saque)

        # =-=-=-=-=-=-=-=-= Widgets Places ==-=-=-=-=-=-=-=-=-=-=-=-
        self.nome_saque_entry.place(x=280, y=200)
        self.conta_saque_entry.place(x=280, y=280)
        self.senha_saque_entry.place(x=280, y=360)
        self.valor_saque_entry.place(x=280, y=440)
        self.check_box_PessoaFisica.place(x=200, y=520)
        self.check_box_PessoaJuridica.place(x=460, y=520)
        self.botão_saque.place(x=290, y=580)

    def verificar_checkbox(self) -> str:
        """Função responsável por validar o resultado dos checkboxes"""
        try:
            pf_valor: int = self.check_box_PessoaFisica.get()
            pj_valor: int = self.check_box_PessoaJuridica.get()

            if pf_valor == 0 and pj_valor == 0:
                raise ValueError('Você não marcou uma das opções: Pessoa Física ou Jurídica.')
            elif pf_valor == 1 and pj_valor == 1:
                raise ValueError('Você selecionou as duas opções (Pessoa Física e Jurídica). '
                                 'Favor, escolher somente uma!')
        except ValueError as erro:
            messagebox.showerror('FALHA NA OPERAÇÃO!', f'{erro}')
            return 'Inválido'
        else:
            match pf_valor:
                case 1:
                    return 'Pessoa Física'

            match pj_valor:
                case 1:
                    return 'Pessoa Jurídica'

    def realizar_saque(self):
        check_box_resultado: str = self.verificar_checkbox()
        bd_cliente_localizado : int = ''
        bd_conta_localizada: int = ''
        conta_saque = ''

        if (not self.nome_saque_entry.get() or not self.conta_saque_entry.get() or not self.senha_saque_entry.get()
                or not self.valor_saque_entry.get()):
            messagebox.showerror('ERRO!', "Você precisa preencher todos os dados!")
        else:
            check_box_valido = False
            match check_box_resultado:
                case 'Inválido':
                    pass
                case 'Pessoa Física':
                    try:
                        for cliente in clientes_pf:
                            if self.nome_saque_entry.get() == cliente.classificacao.nome:
                                bd_cliente_localizado = clientes_pf.index(cliente)

                        for conta in clientes_pf[bd_cliente_localizado].contas:
                            if (int(self.conta_saque_entry.get()) == conta.numero
                                    and self.senha_saque_entry.get() == conta.senha):
                                bd_conta_localizada = clientes_pf[bd_cliente_localizado].contas.index(conta)

                        conta_saque = clientes_pf[bd_cliente_localizado].contas[bd_conta_localizada]
                        check_box_valido = True
                    except Exception:
                        pass

                case 'Pessoa Jurídica':
                    try:
                        for cliente in clientes_pj:
                            if self.nome_saque_entry.get() == cliente.classificacao.nome:
                                bd_cliente_localizado = clientes_pj.index(cliente)

                        for conta in clientes_pj[bd_cliente_localizado].contas:
                            if int(self.conta_saque_entry.get()) == conta.numero and self.senha_saque_entry.get() == conta.senha:
                                bd_conta_localizada = clientes_pj[bd_cliente_localizado].contas.index(conta)
                        conta_saque = clientes_pj[bd_cliente_localizado].contas[bd_conta_localizada]
                        check_box_valido = True
                    except Exception:
                        pass


            if check_box_valido:
                # usar a conta = clientes[cliente_localizado].contas[conta_localizada].saques_realizados

                if conta_saque.saldo == 0:
                    messagebox.showerror('OPERAÇÃO CANCELADA!', 'VOCÊ NÃO POSSUI SALDO SUFICIENTE!')
                elif conta_saque.saques_realizados == conta_saque.limite_de_saque:
                    messagebox.showerror("OPERAÇÃO CANCELADA!",
                                         "VOCÊ ATINGIU O LIMITE DE SAQUES DIÁRIOS PARA ESTA CONTA!")
                else:
                    valor_do_saque = float(self.valor_saque_entry.get())
                    conta_saque.realizar_saque(True, valor_do_saque)
                    conta_saque.contabilizar_saque()
                    messagebox.showinfo("SUCESSO!",
                                        f"Saque realizado com SUCESSO na conta: {conta_saque.numero}\n"
                                                    f"Saldo atual: R$ {conta_saque.saldo}\n"
                                                    f"Saques Restantes: "
                                                    f"{conta_saque.limite_de_saque - conta_saque.saques_realizados}")

                    #=-=-=-=-= Prints para verificação de informação =-=-=-=-=-

                    for transacoes in conta_saque.historico.registros:
                        print(transacoes)
                    print(f'Total de transacoes realizadas {len(conta_saque.historico.registros)}')

                    # =-=-=-=-= Prints para verificação de informação =-=-=-=-=-

            """REFATORAR SAQUE E DEPÓSITO COM OS BANCOS DE DADOS PF E PJ"""

class Janela_Deposito:
    def depositar(self):
        self.janela_depositar = ctk.CTkToplevel()
        self.janela_depositar.geometry("700x720+650+100")
        self.janela_depositar.title("BRASBANK - Janela Depósito")
        self.janela_depositar.resizable(False, False)
        self.depositar_widgets()
        self.janela_depositar.grab_set()
        self.janela_depositar.focus_force()
        self.janela_depositar.mainloop()

    def depositar_widgets(self):

        # =-=-=-=-=-=-=-=-= Criando Bordas e Cabeçalho ==-=-=-=-=-=-=-=-=-=-=-=-
        self.borda_deposito = ctk.CTkFrame(master=self.janela_depositar, width=700, height=720, fg_color='#708090')
        self.borda_deposito.place(x=0, y=0)

        self.segunda_tela_deposito = ctk.CTkFrame(master=self.janela_depositar, width=500, height=500, fg_color="#8FBC8F",
                                         bg_color='#708090')
        self.segunda_tela_deposito.place(x=110, y=140)

        self.cabecalho_deposito = ctk.CTkLabel(master=self.janela_depositar, text='REALIZAR DEPÓSITO', font=('Impact', 20))
        self.cabecalho_deposito.place(x=280, y=130)

        # =-=-=-=-=-=-=-=-= Criando Paineis de Texto ==-=-=-=-=-=-=-=-=-=-=-=-
        self.painel_nome_deposito = ctk.CTkFrame(master=self.janela_depositar, width=98, height=28, fg_color='#708090',
                                                 bg_color="#8FBC8F")
        self.painel_conta_deposito = ctk.CTkFrame(master=self.janela_depositar, width=98, height=28, fg_color='#708090',
                                                  bg_color="#8FBC8F")
        self.painel_senha_deposito = ctk.CTkFrame(master=self.janela_depositar, width=98, height=28, fg_color='#708090',
                                                  bg_color="#8FBC8F")
        self.painel_valor_deposito = ctk.CTkFrame(master=self.janela_depositar, width=98, height=28, fg_color='#708090',
                                                  bg_color="#8FBC8F")

        self.nome_texto_deposito = ctk.CTkLabel(master=self.janela_depositar, text='Nome', bg_color='#708090',
                                                font=('Impact', 14), text_color='#E0FFFF')
        self.conta_texto_deposito = ctk.CTkLabel(master=self.janela_depositar, text='Conta', bg_color='#708090',
                                                 font=('Impact', 14), text_color='#E0FFFF')
        self.senha_texto_deposito = ctk.CTkLabel(master=self.janela_depositar, text='Senha', bg_color='#708090',
                                                 font=('Impact', 14), text_color='#E0FFFF')
        self.valor_texto_deposito = ctk.CTkLabel(master=self.janela_depositar, text='Valor R$', bg_color='#708090',
                                                 font=('Impact', 14), text_color='#E0FFFF')

        # =-=-=-=-=-=-=-=-= Places ==-=-=-=-=-=-=-=-=-=-=-=-
        self.painel_nome_deposito.place(x=200, y=200)
        self.painel_conta_deposito.place(x=200, y=280)
        self.painel_senha_deposito.place(x=200, y=360)
        self.painel_valor_deposito.place(x=200, y=440)

        self.nome_texto_deposito.place(x=220, y=200)
        self.conta_texto_deposito.place(x=220, y=280)
        self.senha_texto_deposito.place(x=220, y=360)
        self.valor_texto_deposito.place(x=220, y=440)

        # =-=-=-=-=-=-=-=-= Criando Widgets para Depósito ==-=-=-=-=-=-=-=-=-=-=-=-
        self.nome_deposito_entry = ctk.CTkEntry(master=self.janela_depositar, width=300, bg_color="#8FBC8F")
        self.conta_deposito_entry = ctk.CTkEntry(master=self.janela_depositar, width=300, bg_color="#8FBC8F")
        self.senha_deposito_entry = ctk.CTkEntry(master=self.janela_depositar, width=300, bg_color="#8FBC8F")
        self.valor_deposito_entry = ctk.CTkEntry(master=self.janela_depositar, width=300, bg_color="#8FBC8F")
        self.check_box_PessoaFisica_Deposito = ctk.CTkCheckBox(master=self.janela_depositar, text='Pessoa Física',
                                                               bg_color="#8FBC8F")
        self.check_box_PessoaJuridica_Deposito = ctk.CTkCheckBox(master=self.janela_depositar, text='Pessoa Jurídica',
                                                                 bg_color="#8FBC8F")
        self.botão_realizar_deposito = ctk.CTkButton(master=self.janela_depositar, text='Realizar Depósito',
                                                     bg_color="#8FBC8F", command=self.realizar_deposito_bancario)


        # =-=-=-=-=-=-=-=-= Widgets Places ==-=-=-=-=-=-=-=-=-=-=-=-
        self.nome_deposito_entry.place(x=280, y=200)
        self.conta_deposito_entry.place(x=280, y=280)
        self.senha_deposito_entry.place(x=280, y=360)
        self.valor_deposito_entry.place(x=280, y=440)
        self.check_box_PessoaFisica_Deposito.place(x=200, y=520)
        self.check_box_PessoaJuridica_Deposito.place(x=460, y=520)
        self.botão_realizar_deposito.place(x=290, y=580)

    def valida_checkbox_deposito(self) -> str:
        """Classe responsável por validar o resultado das checkboxes"""
        try:
            pf_valor_Deposito: int = self.check_box_PessoaFisica_Deposito.get()
            pjvalor_Deposito: int = self.check_box_PessoaJuridica_Deposito.get()

            if pf_valor_Deposito == 0 and pjvalor_Deposito == 0:
                raise ValueError('Você não marcou uma das opções: Pessoa Física ou Jurídica.')
            elif pf_valor_Deposito == 1 and pjvalor_Deposito == 1:
                raise ValueError(
                    'Você selecinou as duas opções (Pessoa Física e Jurídica). Favor, escolher somente uma!')
        except ValueError as erro:
            messagebox.showerror('FALHA NA OPERAÇÃO!', f'{erro}')
            return 'Inválido'
        else:
            match pf_valor_Deposito:
                case 1:
                    return 'Pessoa Física'

            match pjvalor_Deposito:
                case 1:
                    return 'Pessoa Jurídica'

    def realizar_deposito_bancario(self):
        if (not self.nome_deposito_entry.get() or not self.conta_deposito_entry.get()
                or not self.senha_deposito_entry.get() or not self.valor_deposito_entry.get()):
            messagebox.showerror('ERRO!', "Você precisa preencher todos os dados!")
        else:
            check_box_deposito_resultado: str = self.valida_checkbox_deposito()
            cliente_deposito_localizado: int = ''
            conta_deposito_localizada: int = ''

            match check_box_deposito_resultado:
                case 'Inválido':
                    pass
                case 'Pessoa Física':
                    try:
                        for cliente in clientes_pf:
                            if self.nome_deposito_entry.get() == cliente.classificacao.nome:
                                cliente_deposito_localizado = clientes_pf.index(cliente)

                        if cliente_deposito_localizado == '':
                            raise ValueError('Cliente não localizado!')
                    except ValueError as erro:
                        messagebox.showerror('ERRO!', f'{erro}')
                        pass
                    else:
                        try:
                            for conta in clientes_pf[cliente_deposito_localizado].contas:
                                if (int(self.conta_deposito_entry.get()) == conta.numero
                                        and self.senha_deposito_entry.get() == conta.senha):
                                    conta_deposito_localizada = clientes_pf[cliente_deposito_localizado].contas.index(conta)
                            if conta_deposito_localizada == '':
                                raise ValueError('Cliente não localizado!')
                        except ValueError as erro:
                            messagebox.showerror('ERRO!', f'{erro}')
                            pass
                        else:
                            conta_utilizada_dep = clientes_pf[cliente_deposito_localizado].contas[conta_deposito_localizada]
                            valor_deposito = float(self.valor_deposito_entry.get())
                            conta_utilizada_dep.realizar_deposito(True, valor_deposito)
                            print(conta_utilizada_dep.exibe_saldo_tela())
                            messagebox.showinfo('Sucesso!', f'O Depósito no valor de R$ {valor_deposito}'
                                                            f' foi Realizado com Sucesso!')

                            # =-=-=-=-= Prints para verificação de informação =-=-=-=-=-

                            for transacoes in conta_utilizada_dep.historico.registros:
                                print(transacoes)
                            print(f'Total de transacoes realizadas {len(conta_utilizada_dep.historico.registros)}')

                            # =-=-=-=-= Prints para verificação de informação =-=-=-=-=-

                case 'Pessoa Jurídica':
                    try:
                        for cliente in clientes_pj:
                            if self.nome_deposito_entry.get() == cliente.classificacao.nome:
                                cliente_deposito_localizado = clientes_pj.index(cliente)
                        if cliente_deposito_localizado == '':
                            raise ValueError('Cliente não localizado!')
                    except ValueError as erro:
                        messagebox.showerror('ERRO!', f'{erro}')
                        pass

                    else:
                        try:
                            for conta in clientes_pj[cliente_deposito_localizado].contas:
                                if (int(self.conta_deposito_entry.get()) == conta.numero
                                        and self.senha_deposito_entry.get() == conta.senha):
                                    conta_deposito_localizada = clientes_pj[cliente_deposito_localizado].contas.index(conta)
                            if conta_deposito_localizada == '':
                                raise ValueError('Cliente não localizado!')
                        except ValueError as erro:
                            messagebox.showerror('ERRO!', f'{erro}')
                            pass
                        else:
                            conta_utilizada_dep = clientes_pj[cliente_deposito_localizado].contas[conta_deposito_localizada]
                            valor_deposito = float(self.valor_deposito_entry.get())
                            conta_utilizada_dep.realizar_deposito(True, valor_deposito)
                            print(conta_utilizada_dep.exibe_saldo_tela())
                            messagebox.showinfo('Sucesso!', f'O Depósito no valor de R$ {valor_deposito}'
                                                            f' foi Realizado com Sucesso!')


                            # =-=-=-=-= Prints para verificação de informação =-=-=-=-=-

                            for transacoes in conta_utilizada_dep.historico.registros:
                                print(transacoes)
                            print(f'Total de transacoes realizadas {len(conta_utilizada_dep.historico.registros)}')

                            # =-=-=-=-= Prints para verificação de informação =-=-=-=-=-

class Janela_Ver_Saldo:
    def iniciar_consulta(self):
        self.janela_vs = ctk.CTkToplevel()
        self.janela_vs.geometry("700x720+650+100")
        self.janela_vs.title('BRASBANK - Consulta de Saldo !')
        self.janela_vs.resizable(False, False)
        self.widgets_consulta()
        self.janela_vs.focus_force()
        self.janela_vs.grab_set()
        self.janela_vs.mainloop()

    def widgets_consulta(self):

        # =-=-=-=-==-=-=-= Criando Painéis =-=-====-=-=-=-=-=-=-==-=-=-=
        self.nome_painel_consulta = ctk.CTkFrame(master=self.janela_vs, width=68, height=28, fg_color='#708090')
        self.num_da_conta_consulta = ctk.CTkFrame(master=self.janela_vs, width=98, height=28, fg_color='#708090')
        self.senha_consulta = ctk.CTkFrame(master=self.janela_vs, width=68, height=28, fg_color='#708090')


        self.nome_texto_consulta = ctk.CTkLabel(master=self.janela_vs, text='Nome', font=('Impact', 14),
                                                bg_color='#708090',
                                                text_color='white')
        self.num_da_conta_texto_consulta = ctk.CTkLabel(master=self.janela_vs, text='Núm Da Conta', font=('Impact', 14),
                                                        bg_color='#708090',
                                          text_color='white')
        self.senha_texto_consulta = ctk.CTkLabel(master=self.janela_vs, text='Senha', font=('Impact', 14),
                                                 bg_color='#708090',
                                                 text_color='white')

        # =-=-=-=-==-=-=-= Places =-=-====-=-=-=-=-=-=-==-=-=-=
        self.nome_painel_consulta.place(x=180, y=230)
        self.nome_texto_consulta.place(x=190, y=230)

        self.num_da_conta_consulta.place(x=160, y=310)
        self.num_da_conta_texto_consulta.place(x=170, y=310)

        self.senha_consulta.place(x=180, y=390)
        self.senha_texto_consulta.place(x=190, y=390)



        #-=-=-=-=-=-= Criando os Widgets para consulta =-==-=-=-=-=-==-=
        self.nome_consulta = ctk.CTkEntry(master=self.janela_vs)
        self.numero_da_conta_consulta =ctk.CTkEntry(master=self.janela_vs)
        self.senha_consulta = ctk.CTkEntry(master=self.janela_vs)
        self.drop_menu_secao = ctk.CTkOptionMenu(master=self.janela_vs,
                                           values=['Pessoa Física', 'Pessoa Jurídica'])
        self.botao_consultar = ctk.CTkButton(master=self.janela_vs, text='Ver Saldo!', command=self.exibir_saldo)

        # -=-=-=-=-=-= Places =-==-=-=-=-=-==-=
        self.nome_consulta.place(x=280, y=230)
        self.numero_da_conta_consulta.place(x=280, y=310)
        self.senha_consulta.place(x=280, y=390)
        self.drop_menu_secao.place(x=280, y=450)
        self.botao_consultar.place(x=280, y=550)

    def tela_saldo(self, saldo):
        self.tela = ctk.CTkToplevel()
        self.tela.geometry("700x720+650+100")
        self.tela.title('BRASBANK - Seu Saldo !')
        self.tela.resizable(False, False)

        self.borda = ctk.CTkFrame(master=self.tela, width=700, height=720, fg_color='#708090')
        self.borda.place(x=0, y=0)

        self.segunda_tela = ctk.CTkFrame(master=self.tela, width=500, height=500, fg_color="#8FBC8F", bg_color='#708090')
        self.segunda_tela.place(x=110, y=140)

        self.saldo_cabecalho = ctk.CTkLabel(master=self.tela, text='SALDO ATUAL', font=('Impact', 20))
        self.saldo_cabecalho.place(x=310, y=130)

        self.saldo_texto = ctk.CTkLabel(master=self.tela, text=f'R$ {float(saldo):.2f}', font=('System', 40), bg_color="#8FBC8F")
        self.saldo_texto.place(x=250, y=360)

        self.tela.focus_force()
        self.tela.grab_set()
        self.tela.mainloop()


    def exibir_saldo(self):
        if not self.nome_consulta.get() or not self.numero_da_conta_consulta.get() or not self.senha_consulta.get():
            messagebox.showerror("Erro!","Você precisa preencher todos os campos.")
        else:
            dados_validos = True
            secao: str = self.drop_menu_secao.get()

            cliente_localizado: int = ''
            conta_localizada: int = ''

            match secao:
                case 'Pessoa Física':
                    try:
                        for cliente in clientes_pf:
                            if self.nome_consulta.get() == cliente.classificacao.nome:
                                cliente_localizado = clientes_pf.index(cliente)

                                break
                        if cliente_localizado == '':
                            raise ValueError('Cliente não Localizado!')

                    except ValueError as erro:
                        messagebox.showerror("ERRO!", f'{erro}')
                        dados_validos = False
                    else:
                        try:
                            for conta in clientes_pf[cliente_localizado].contas:
                                if (int(self.numero_da_conta_consulta.get()) == conta.numero
                                        and self.senha_consulta.get() == conta.senha):
                                    conta_localizada = clientes_pf[cliente_localizado].contas.index(conta)

                                    break
                            if conta_localizada == '':
                                raise ValueError('Cliente não localizado!')
                        except ValueError as erro:
                            messagebox.showerror("ERRO", f'{erro}')
                            dados_validos = False

                case 'Pessoa Jurídica':
                    try:
                        for cliente in clientes_pj:
                            if (self.nome_consulta.get() == cliente.classificacao.nome
                                    and cliente.classificacao.__class__.__name__ == 'Pessoa_Juridica'):
                                cliente_localizado = clientes_pj.index(cliente)
                        if cliente_localizado == '':
                            raise ValueError('Cliente não localizado!')

                    except ValueError as erro:
                        messagebox.showerror("ERRO", f'{erro}')
                        dados_validos = False
                    else:
                        try:
                            for conta in clientes_pj[cliente_localizado].contas:
                                if (int(self.numero_da_conta_consulta.get()) == conta.numero
                                        and self.senha_consulta.get() == conta.senha):
                                    conta_localizada = clientes_pj[cliente_localizado].contas.index(conta)
                            if conta_localizada == '':
                                raise ValueError('Cliente não localizado!')

                        except ValueError as erro:
                            messagebox.showerror("ERRO", f'{erro}')
                            dados_validos = False

            match dados_validos:
                case True:
                    if secao == 'Pessoa Física':
                        conta_utilizada = clientes_pf[cliente_localizado].contas[conta_localizada]
                        saldo = str(conta_utilizada.exibe_saldo_tela())
                        self.tela_saldo(saldo)
                    elif secao == 'Pessoa Jurídica':
                        conta_utilizada = clientes_pj[cliente_localizado].contas[conta_localizada]
                        saldo = str(conta_utilizada.exibe_saldo_tela())
                        self.tela_saldo(saldo)
                case False:
                    messagebox.showerror('ERRO', 'Conta não localizada!\n'
                                                 'Verifique os dados e tente novamente')




class Formulario_Pesssoa_Juridica:
    """Classe para a janela de cadastro de pessoa Jurídica"""
    def __init__(self):
        self.formulario_pj = ctk.CTkToplevel()
        self.formulario_pj.geometry("700x720+650+100")
        self.formulario_pj.title('BRASBANK - Janela de Formulário para Cadastro !')
        self.formulario_pj.resizable(False, False)
        self.formulario_widgets_pj()
        self.formulario_pj.grab_set()
        self.formulario_pj.focus_force()
        self.formulario_pj.mainloop()

    def realizar_cadastro_pj(self):
        if (not self.nome_entry_pj.get() or not self.cnpj.get() or not self.data_nascimento_pj.get()
                or not self.endereco_pj.get() or not self.senha_pj.get()):
            tk.messagebox.showerror('Erro!', 'Você precisa preencher todos os dados!')
        else:
            possui_conta_pj = False

            match len(clientes_pj):
                case 0:
                    cliente = Cliente(self.endereco_pj.get())
                    cliente.classificacao = Pessoa_Juridica(self.nome_entry_pj.get(), self.cnpj.get(),
                                                            self.data_nascimento_pj.get())
                    conta = Conta_Corrente.gerar_conta(numero=randint(1, 10000), senha=self.senha_pj.get(),
                                                       cliente=cliente)
                    cliente.adicionar_conta(conta)
                    clientes_pj.append(cliente)
                    self.limpa_entrys_pj()
                    tk.messagebox.showinfo("Sucesso",
                                f'Cadastro realizado com sucesso\nAnote o Nº da sua conta:  {conta.numero}')
                    print(clientes_pj)

                case _ as status if status == len(clientes_pj) > 0:
                    for cliente in clientes_pj:
                        if cliente.classificacao.nome == self.nome_entry_pj.get():
                            possui_conta_pj = True
                            break

                    match possui_conta_pj:
                        case True:
                            cliente = Cliente(self.endereco_pj.get())
                            cliente.classificacao = Pessoa_Juridica(self.nome_entry_pj.get(), self.cnpj.get(),
                                                                    self.data_nascimento_pj.get())
                            conta = Conta_Corrente.gerar_conta(numero=randint(1, 10000), senha=self.senha_pj.get(),
                                                               cliente=cliente)
                            for cliente in clientes_pj:
                                if cliente.classificacao.nome == self.nome_entry_pj.get():
                                    cliente.adicionar_conta(conta)
                                    print(f'Contas do {cliente.classificacao.nome}: {cliente.contas}')
                                    break
                            nome = self.nome_entry_pj.get()
                            self.limpa_entrys_pj()
                            messagebox.showinfo("SUCESSO!", f"{nome.upper()}\nSua nova conta de Nº "
                                                            f"{conta.numero} foi cadastrada com sucesso!")
                            print(clientes_pj)

                        case False:
                            cliente = Cliente(self.endereco_pj.get())
                            cliente.classificacao = Pessoa_Juridica(self.nome_entry_pj.get(), self.cnpj.get(),
                                                                    self.data_nascimento_pj.get())
                            conta = Conta_Corrente.gerar_conta(numero=randint(1, 10000), senha=self.senha_pj.get(),
                                                               cliente=cliente)
                            cliente.adicionar_conta(conta)
                            clientes_pj.append(cliente)
                            self.limpa_entrys_pj()
                            tk.messagebox.showinfo("Sucesso",
                                f'Cadastro realizado com sucesso\nAnote o Nº da sua conta:  {conta.numero}')
                            print(clientes_pj)



    def formulario_widgets_pj(self):
        # -=-=-=-=-=-= Widgets Visuais =-=-=-=-=-=-=-=-=-=

        self.nome_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.nome_texto_pj = ctk.CTkLabel(master=self.formulario_pj, text='Nome', font=('Impact', 14), bg_color='#708090',
                                          text_color='white')
        self.cnpj_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.cnpj_texto_pj = ctk.CTkLabel(master=self.formulario_pj, text='CNPJ', font=('Impact', 14), bg_color='#708090',
                                          text_color='white')

        self.dt_nascimento_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.dt_nascimento_texto_pj = ctk.CTkLabel(master=self.formulario_pj, text='DT Nascimento', font=('Impact', 10),
                                                   bg_color='#708090',
                                                   text_color='white')

        self.endereco_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.endereco_texto_pj= ctk.CTkLabel(master=self.formulario_pj, text='Endereço', font=('Impact', 14),
                                             bg_color='#708090',
                                             text_color='white')

        self.senha_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.senha_texto_pj = ctk.CTkLabel(master=self.formulario_pj, text='Senha', font=('Impact', 14),
                                           bg_color='#708090',
                                           text_color='white')


        # =-=-=-=-=-= Places =-=-==-=-=-=-=-=-
        self.nome_painel_pj.place(x=82, y=160)
        self.nome_texto_pj.place(x=92, y=160)
        self.cnpj_painel_pj.place(x=82, y=230)
        self.cnpj_texto_pj.place(x=92, y=230)
        self.dt_nascimento_painel_pj.place(x=336, y=229)
        self.dt_nascimento_texto_pj.place(x=340, y=229)
        self.endereco_painel_pj.place(x=82, y=330)
        self.endereco_texto_pj.place(x=92, y=330)
        self.senha_painel_pj.place(x=165, y=420)
        self.senha_texto_pj.place(x=180, y=420)

        # -=-=-=-=-=-=-=-=-= Widgets Cadastrais -=-=-=-=-=-=-=-=-=
        self.nome_entry_pj = ctk.CTkEntry(master=self.formulario_pj, width=400)
        self.cnpj= ctk.CTkEntry(master=self.formulario_pj)
        self.data_nascimento_pj = ctk.CTkEntry(master=self.formulario_pj)
        self.endereco_pj = ctk.CTkEntry(master=self.formulario_pj, width=400)
        self.senha_pj = ctk.CTkEntry(master=self.formulario_pj, width=220)
        self.botao_confirmar_cadastro_pj = ctk.CTkButton(master=self.formulario_pj, text='Cadastrar',
                                                      command=self.realizar_cadastro_pj)

        # -=-=-=-=-=-=-=-=-= Places -=-=-=-=-=-=-=-=-=
        self.nome_entry_pj.place(x=170, y=160)
        self.cnpj.place(x=170, y=230)
        self.data_nascimento_pj.place(x=430, y=230)
        self.endereco_pj.place(x=170, y=330)
        self.senha_pj.place(x=250, y=420)
        self.botao_confirmar_cadastro_pj.place(x=284, y=520)

    def limpa_entrys_pj(self):
        self.nome_entry_pj.delete(0, 'end')
        self.cnpj.delete(0, 'end')
        self.data_nascimento_pj.delete(0, 'end')
        self.endereco_pj.delete(0, 'end')
        self.senha_pj.delete(0, 'end')


class Formulario_Pessoa_Fisica:
    """Classe para a janela de cadastro de pessoa Física"""
    def __init__(self):
        self.formulario_pf = ctk.CTkToplevel()
        self.formulario_pf.geometry('700x720+650+100')
        self.formulario_pf.title('BRASBANK - Janela de Formulário para Cadastro!')
        self.formulario_pf.resizable(False, False)
        self.formulario_widgets()
        self.formulario_pf.grab_set()
        self.formulario_pf.focus_force()
        self.formulario_pf.mainloop()

    def realizar_cadastro(self):
        if (not self.nome_entry.get() or not self.cpf.get() or not self.data_nascimento.get() or not self.endereco.get()
                or not self.senha.get()):
            tk.messagebox.showerror('Erro!', 'Você precisa preencher todos os dados!')
        else:
            # -=-=-=-=-=- Cadastrando Cliente Pessoa Física e Conta Bancária -=-=-=-=-=-
            possui_conta = False
            match len(clientes_pf):
                case 0:
                    cliente = Cliente(self.endereco.get())
                    cliente.classificacao = Pessoa_Fisica(self.nome_entry.get(), self.cpf.get(), self.data_nascimento.get())
                    conta = Conta_Corrente.gerar_conta(numero=randint(1, 10000), senha=self.senha.get(), cliente=cliente)
                    cliente.adicionar_conta(conta)
                    clientes_pf.append(cliente)
                    tk.messagebox.showinfo("Sucesso",
                                           f'Cadastro realizado com sucesso\nAnote o Nº da sua conta: {conta.numero}!')
                    print(clientes_pf)
                    self.limpa_entrys()
                case _ as status if status == len(clientes_pf) > 0:
                    for cliente in clientes_pf:
                        if cliente.classificacao.nome == self.nome_entry.get():
                            possui_conta = True
                            break

                    match possui_conta:
                        case True:
                            cliente = Cliente(self.endereco.get())
                            cliente.classificacao = Pessoa_Fisica(self.nome_entry.get(), self.cpf.get(),
                                                                  self.data_nascimento.get())
                            conta = Conta_Corrente.gerar_conta(numero=randint(1, 10000), senha=self.senha.get(),
                                                               cliente=cliente)
                            for cliente in clientes_pf:
                                if cliente.classificacao.nome == self.nome_entry.get():
                                    cliente.adicionar_conta(conta)
                                    print(f'Contas do {cliente.classificacao.nome}: {cliente.contas}')
                                    break
                            nome = self.nome_entry.get()
                            self.limpa_entrys()
                            messagebox.showinfo("SUCESSO!", f"{nome.upper()}\nSua nova conta de Nº "
                                                            f"{conta.numero} foi cadastrada com sucesso!")
                            print(clientes_pf)

                        case False:
                            cliente = Cliente(self.endereco.get())
                            cliente.classificacao = Pessoa_Fisica(self.nome_entry.get(), self.cpf.get(),
                                                                  self.data_nascimento.get())
                            conta = Conta_Corrente.gerar_conta(numero=randint(1, 10000), senha=self.senha.get(),
                                                               cliente=cliente)
                            cliente.adicionar_conta(conta)
                            clientes_pf.append(cliente)
                            tk.messagebox.showinfo("Sucesso",
                                f'Cadastro realizado com sucesso\nAnote o Nº da sua conta: {conta.numero}!')
                            print(clientes_pf)
                            self.limpa_entrys()


    def limpa_entrys(self):
        self.nome_entry .delete(0, 'end')
        self.cpf.delete(0, 'end')
        self.data_nascimento.delete(0, 'end')
        self.endereco.delete(0, 'end')
        self.senha.delete(0, 'end')


    def formulario_widgets(self):

        #-=-=-=-=-=-= Widgets Visuais =-=-=-=-=-=-=-=-=-=

        self.nome_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.nome_texto = ctk.CTkLabel(master=self.formulario_pf, text='Nome', font=('Impact', 14), bg_color='#708090',
                                       text_color='white')
        self.cpf_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.cpf_texto = ctk.CTkLabel(master=self.formulario_pf, text='CPF', font=('Impact', 14), bg_color='#708090',
                                       text_color='white')

        self.dt_nascimento_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.dt_nascimento_texto = ctk.CTkLabel(master=self.formulario_pf, text='DT Nascimento', font=('Impact', 10),
                                                bg_color='#708090',
                                                text_color='white')

        self.endereco_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.endereco_texto= ctk.CTkLabel(master=self.formulario_pf, text='Endereço', font=('Impact', 14),
                                         bg_color='#708090',
                                         text_color='white')

        self.senha_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.senha_texto = ctk.CTkLabel(master=self.formulario_pf, text='Senha', font=('Impact', 14),
                                         bg_color='#708090',
                                         text_color='white')

        # =-=-=-=-=-= Places =-=-==-=-=-=-=-=-
        self.nome_painel.place(x=82, y=160)
        self.nome_texto.place(x=92, y=160)
        self.cpf_painel.place(x=82, y=230)
        self.cpf_texto.place(x=92, y=230)
        self.dt_nascimento_painel.place(x=336, y=229)
        self.dt_nascimento_texto.place(x=340, y=229)
        self.endereco_painel.place(x=82, y=330)
        self.endereco_texto.place(x=92, y=330)
        self.senha_painel.place(x=165, y=420)
        self.senha_texto.place(x=180, y=420)


        # -=-=-=-=-=-=-=-=-= Widgets Cadastrais -=-=-=-=-=-=-=-=-=
        self.nome_entry = ctk.CTkEntry(master=self.formulario_pf, width=400)
        self.cpf = ctk.CTkEntry(master=self.formulario_pf)
        self.data_nascimento = ctk.CTkEntry(master=self.formulario_pf)
        self.endereco = ctk.CTkEntry(master=self.formulario_pf, width=400)
        self.senha = ctk.CTkEntry(master=self.formulario_pf, width=220)
        self.botao_confirmar_cadastro = ctk.CTkButton(master=self.formulario_pf, text='Cadastrar',
                                                      command=self.realizar_cadastro)


        # -=-=-=-=-=-=-=-=-= Places -=-=-=-=-=-=-=-=-=
        self.nome_entry.place(x=170, y=160)
        self.cpf.place(x=170, y=230)
        self.data_nascimento.place(x=430, y=230)
        self.endereco.place(x=170, y=330)
        self.senha.place(x=250, y=420)
        self.botao_confirmar_cadastro.place(x=284, y=520)






class Cadastro_de_Conta:
    """Classe  com a janela para escolha de pessoa física ou jurídica"""
    def cadastrar(self):
        self.janela_cadastro = ctk.CTkToplevel()
        self.janela_cadastro.title('BRASBANK - Bem vindo ao sistema de cadastro! V: 1.0 Made By: FelRFDev!')
        self.janela_cadastro.geometry('700x720+650+100')
        self.janela_cadastro.resizable(False, False)
        self.widgets_de_cadastro()
        self.janela_cadastro.grab_set()
        self.janela_cadastro.focus_force()
        self.janela_cadastro.mainloop()

    def realizar_cadastro(self):
        if self.drop_menu.get() == 'Pessoa Física':
            self.janela_cadastro.destroy()
            Formulario_Pessoa_Fisica()
        elif self.drop_menu.get() == 'Pessoa Jurídica':
            self.janela_cadastro.destroy()
            Formulario_Pesssoa_Juridica()
        
    def widgets_de_cadastro(self):
        self.escolha = ''
        self.moedas_imagem = tk.PhotoImage(master=self.janela_cadastro, data=moedas)
        self.moedas_painel = tk.Canvas(master=self.janela_cadastro, width=720, height=720)
        self.moedas_painel.create_image((self.moedas_imagem.width() / 2, self.moedas_imagem.height() / 2),
                                        image=self.moedas_imagem)

        self.painel_barra = tk.Canvas(master=self.janela_cadastro, width=720, height=60, background='#727272')

        self.painel_dp_menu = ctk.CTkFrame(master=self.janela_cadastro, width=400, height=400, fg_color='#708090')
        self.drop_menu = ctk.CTkOptionMenu(master=self.janela_cadastro,
                                           bg_color='#708090', 
                                           values=['Pessoa Física', 'Pessoa Jurídica'])
        
        self.botao_cadastrar_escolha = ctk.CTkButton(master=self.janela_cadastro, text='Cadastrar', bg_color='#708090',
                                                     command=self.realizar_cadastro)

        
        
        self.painel_barra.place(x=-2, y=0)
        self.painel_dp_menu.place(x=160, y=150)
        self.drop_menu.place(x=290, y=290)
        self.botao_cadastrar_escolha.place(x=290, y=390)
        self.moedas_painel.place(x=0, y=0)




class Janela_Principal(Cadastro_de_Conta, Formulario_Pessoa_Fisica, Janela_Ver_Saldo, Janela_Deposito, Janela_Saque):
    """Classe que origina a janela principal"""
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry('699x720+650+100')
        self.root.title('BRASBANK - Caixa Eletrônico! - Seja bem vindo! V: 1.0 Made By: FelRFDev!')
        self.root.resizable(False, False)
        self.root._set_appearance_mode('dark')
        self.widgets()
        self.root.mainloop()
    
    def widgets(self):
        # -=-===-== Criando os Widgets =-=-=-=-=-=
        self.painel1 = tk.Canvas(master=self.root, width=240, height=840, background='#727272', highlightthickness=0)
        self.criar_conta = ctk.CTkButton(master=self.root, text='Criar Conta', width=120, font=('Impact',20),  height=100,
                                         bg_color='#727272', command=self.cadastrar)
        self.ver_saldo = ctk.CTkButton(master=self.root, text='Ver Saldo', font=('Impact',20), width=120, height=100,
                                       bg_color='#727272', command=self.iniciar_consulta)
        self.fazer_deposito = ctk.CTkButton(master=self.root, text='Realizar\nDepósito', font=('Impact',20), width=120,
                                            height=100, bg_color='#727272', command=self.depositar)
        self.fazer_saque = ctk.CTkButton(master=self.root, text='Realizar\nSaque', width=120, font=('Impact',20),
                                         height=100, bg_color='#727272', command=self.sacar)

        self.banner2 = tk.PhotoImage(master=self.root, data=banner_inicial)
        self.banner2_canvas = tk.Canvas(master=self.root, width=500, height=500, highlightthickness=1)
        self.banner2_canvas.create_image((self.banner2.width()/2, self.banner2.height()/2),image=self.banner2)

        self.banner_banco=tk.PhotoImage(master=self.root, data=banner_do_banco)
        self.banner_banco_canvas = tk.Canvas(master=self.root, width=710, height=233, highlightthickness=1)
        self.banner_banco_canvas.create_image((self.banner_banco.width()/2, self.banner_banco.height()/2),
                                              image=self.banner_banco)
        

        # -=-===-== Posicionando os Widgets =-=-=-=-=-=
        
        self.banner_banco_canvas.place(x=-1, y=-10)
        self.banner2_canvas.place(x=200, y=220)
        self.criar_conta.place(x=30, y=240)
        self.ver_saldo.place(x=30, y=360)
        self.fazer_deposito.place(x=30, y=480)
        self.fazer_saque.place(x=30, y=600)
        self.painel1.place(x=0, y=0)


if __name__ == '__main__':
    janela1 = Janela_Principal()
