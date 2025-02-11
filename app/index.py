#tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#SqLite
import sqlite3

#class
class index():
    #atributos

    def head(self):
        self.frame_head = ttk.Frame(self.root)
        self.frame_head.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        self.titulo = ttk.Label(self.frame_head, text="Lista de tarefas", font=("Stencil", 31, "normal"))
        self.titulo.place(relx=0.1, rely=0.5)
        
    def main(self):
        self.frame_main = ttk.Frame(self.root)
        self.frame_main.place(relx=0, rely=0.2, relheight=0.5, relwidth=1) 
    
       
        self.logar = ttk.Button(self.frame_main, text="Logar", bootstyle=(PRIMARY, OUTLINE))
        self.logar.place(relx=0.32, rely=0.25, relheight=0.15, relwidth=0.4)
        
        self.cadastrar = ttk.Button(self.frame_main, text="Cadastra-se", bootstyle=(SUCCESS, OUTLINE))
        self.cadastrar.place(relx=0.32, rely=0.5, relheight=0.15, relwidth=0.4)
        
        self.descricao = ttk.Label(self.frame_main, text="Bem vindo(a) a sua lista de tarefas!", font=("Arial", 12, "bold"))
        self.descricao.place(relx=0.22, rely=0.8)
        
    def footer(self):
        self.frame_footer = ttk.Frame(self.root)
        self.frame_footer.place(relx=0, rely=0.7, relheight=1, relwidth=1)
        
        self.nome = ttk.Label(self.frame_footer, text="@p._uchoa", font=("Arial", 10, "bold"))
        self.nome.place(relx=0.43,rely=0.2)
        
index()
    