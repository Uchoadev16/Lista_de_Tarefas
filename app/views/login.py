#importanto tudo da biblioteca tkinter
from tkinter import *

#criando a class interface_login herdada da class Frame
class interface_login(Frame):
    #contrutor
    def __init__(self):
        #pegando o construtor da class Frame
        Frame.__init__(self)

        #configurando a tela
        self.master.title("Login")
        self.master.geometry("450x600")
        self.master.iconbitmap("C:/Users/pedro/OneDrive/Área de Trabalho/Python/projetos/Lista_de_Tarefas/app/assets/img/icon_gerenciador.ico")
        
        #frames
        self.header = Frame()
        self.main = Frame()
        self.button = Frame()
        self.footer = Frame()
        self.header.pack()
        self.main.pack()
        self.button.pack()
        self.footer.pack()
        
        #header
        self.login = Label(self.header, text="Login")
        self.login.pack()
        
        #main
        self.email = Label(self.main, text="Email:")
        self.email_input = Entry(self.main)
        self.senha = Label(self.main, text="Senha:")
        self.senha_input = Entry(self.main)
        
        self.email.grid(row=0, column=0)
        self.email_input.grid(row=0, column=1)
        self.senha.grid(row=1, column=0)
        self.senha_input.grid(row=1, column=1)
        
        self.botao = Button(self.button, text="Entrar", command=self.logar)
        self.sair = Button(self.button, text="Sair", command=self.master.quit)
        self.botao.pack(side='left', padx=5)
        self.sair.pack(side='right')
        
        #footer
        self.footer = Label(self.footer, text="@p._uchoa")
        self.footer.pack(side='bottom')
        mainloop()
    def logar(self):
        email = self.email_input.get()
        senha = self.senha_input.get()

interface_login()