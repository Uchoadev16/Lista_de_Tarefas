#tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#SqLite
import sqlite3

class cadastro:
    #atributos
    root = ttk.Window("Lista de tarefas", themename="superhero")
    
    #construtor
    def __init__(self):
        self.tela()
        self.head()
        self.main()
        self.footer()
        self.root.mainloop()
        
    #metodos
    def tela(self):
        
        self.root.iconbitmap("app/assets/img/icone.ico")
        self.root.geometry("550x700")
        self.root.resizable(True, True)
        self.root.maxsize(width=550, height=700)
        self.root.minsize(width=550, height=700)
        
    def head(self):
        
        self.frame_head = ttk.Frame(self.root)
        self.frame_head.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        self.titulo = ttk.Label(self.frame_head, text="Cadastro", font=("Stencil", 32, "normal"))
        self.titulo.place(relx=0.27, rely=0.5)
        
    def main(self):
        
        self.frame_main = ttk.Frame(self.root)
        self.frame_main.place(relx=0, rely=0.2, relheight=0.5, relwidth=1) 
        
    def footer(self):
        self.frame_footer = ttk.Frame(self.root)
        self.frame_footer.place(relx=0, rely=0.7, relheight=1, relwidth=1)
        
        self.nome = ttk.Label(self.frame_footer, text="@p._uchoa", font=("Arial", 10, "bold"))
        self.nome.place(relx=0.43,rely=0.2)
        
cadastro()