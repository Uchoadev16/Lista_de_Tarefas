#tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#SqLite
import sqlite3

#class
class index():
    #atributos
    root = ttk.Tk()
    #construtor
    def __init__(self):
        
        self.tela()
        self.head()
        self.main()
        self.footer()
        self.root.mainloop()
    #metodos
    def tela(self):
        
        self.root.Style("darkly")
        self.root.title("Lista de Tarefas")
        self.root.iconbitmap("app/assets/img/icone.ico")
        self.root.configure(background="#010409")
        self.root.geometry("450x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=450, height=600)
        self.root.minsize(width=450, height=600)
    def head(self):
        
        self.frame_head = Frame(self.root, bg="#010409")
        self.frame_head.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        self.titulo = Label(self.frame_head, text="Lista de tarefas", fg="white", bg="#010409", font=("Stencil", 30, "bold"))
        self.titulo.place(relx=0.1, rely=0.5)
    def main(self):
    
        self.frame_main = Frame(self.root, bg="#010409")
        self.frame_main.place(relx=0, rely=0.2, relheight=0.5, relwidth=1) 
        
        self.logar = ttk.Button(self.frame_main, text="Logar", bootstyle=SUCCESS)
        self.logar.place(relx=0.43, rely=0.3)
        
        self.cadastrar = Button(self.frame_main, text="Cadastra-se", font=("Arial", 15, "bold"), bg="white")
        self.cadastrar.place(relx=0.37, rely=0.5)
        
        self.descricao = Label(self.frame_main, text="Bem vindo(a) a sua lista de tarefas!", bg="#010409", fg="white", font=("Arial", 12, "bold"))
        self.descricao.place(relx=0.22, rely=0.7)
    def footer(self):
        
        self.frame_footer = Frame(self.root, bg="#010409")
        self.frame_footer.place(relx=0, rely=0.7, relheight=1, relwidth=1)
        
        self.nome = Label(self.frame_footer, text="@p._uchoa", font=("Arial", 10, "bold"), fg="white", bg="#010409")
        self.nome.pack(anchor="center", pady=140)

index()
    