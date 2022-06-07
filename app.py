from tkinter import *
import banco


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack(ipadx=20)

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(ipadx=20)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(ipadx=40)

        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(ipadx=20)

        self.quintoContainer = Frame(master)
        self.quintoContainer.pack(ipadx=20)

        self.sextoContainer = Frame(master)
        self.sextoContainer.pack(ipadx=20)

        self.titulo = Label(self.primeiroContainer, text="Insira os dados do paciente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack(side=LEFT)

        # Entrada de Nome
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=RIGHT)


        # Entrada de CPF
        self.nomeLabel = Label(self.terceiroContainer,text="CPF", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.cpf = Entry(self.terceiroContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=RIGHT)


        # Entrada de Data de Nascimento
        self.nomeLabel = Label(self.quartoContainer,text="Data de Nascimento", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.data_de_nascimento = Entry(self.quartoContainer)
        self.data_de_nascimento["width"] = 30
        self.data_de_nascimento["font"] = self.fontePadrao
        self.data_de_nascimento.pack(side=RIGHT)

        self.responsavel_aplicacao = Label(self.quintoContainer, text="Responsável pela Aplicação", font=self.fontePadrao)
        self.responsavel_aplicacao.pack(side=LEFT)

        self.responsavel_aplicacao = Entry(self.quintoContainer)
        self.responsavel_aplicacao["width"] = 30
        self.responsavel_aplicacao["font"] = self.fontePadrao
        self.responsavel_aplicacao.pack(side=RIGHT)

        self.autenticar = Button(self.sextoContainer)
        self.autenticar["text"] = "Registrar"
        self.autenticar["font"] = ("Calibri", "10", "bold")
        self.autenticar["width"] = 20
        self.autenticar["command"] = self.validacoes
        self.autenticar.pack()

        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()


    def verificanome(self):
        nome = self.nome.get()

        validationDigits = nome.isdigit()
        if validationDigits:
            self.mensagem["text"] = "NOME INVÁLIDO"

    def verificacpf(self):
        CPF = self.cpf.get()
        if len(CPF) < 11 or len(CPF) > 11 :
            self.mensagem["text"] = "CPF INVÁLIDO"
        
    def verificadata_de_nascimento(self):
        data_de_nascimento = self.data_de_nascimento.get()
        validationDigits = data_de_nascimento.isdigit()
        if validationDigits == False:
            self.mensagem["text"] = "DATA DE NASCIMENTO INVÁLIDA"
        else:
            print("")
        
    def verificaresponsavel_aplicacao(self):
        responsavel_aplicacao= self.responsavel_aplicacao.get()
        validationDigits = responsavel_aplicacao.isdigit()
        if validationDigits:
            self.mensagem["text"] = "RESPONSÁVEL INVÁLIDO"

    def validacoes(self):
        self.mensagem["text"] = ""
        db = banco.Database('vacinacao.db')

        db.cadastro(self.nome.get(), self.cpf.get(), self.data_de_nascimento.get(), self.responsavel_aplicacao.get())
        db.leitura()

        self.verificanome()
        self.verificacpf()
        self.verificadata_de_nascimento()
        self.verificaresponsavel_aplicacao()

root = Tk()
Application(root)
root.mainloop()