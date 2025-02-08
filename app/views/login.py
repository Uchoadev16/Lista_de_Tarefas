#tkinter
import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#SqLite
import sqlite3

#funções


class login:
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

        self.titulo = ttk.Label(self.frame_head, text="Login", font=("Stencil", 32, "normal"))
        self.titulo.place(relx=0.35, rely=0.5)
        
    def main(self):
        
        self.frame_main = ttk.Frame(self.root)
        self.frame_main.place(relx=0, rely=0.2, relheight=0.5, relwidth=1)
        
        self.label_email = ttk.Label(self.frame_main, text="E-mail:", font=("Arial", 15, "normal"))
        self.label_email.place(relx=0.14, rely=0.24)
        
        self.input_email = ttk.Entry(self.frame_main, font=("Arial", 12, "normal"))
        self.input_email.place(relx=0.25, rely=0.25, relheight=0.15, relwidth=0.5)
        
        self.label_senha = ttk.Label(self.frame_main, text="Senha:", font=("Arial", 15, "normal"))
        self.label_senha.place(relx=0.14, rely=0.54)
        
        self.input_senha = ttk.Entry(self.frame_main, font=("Arial", 12, "normal"))
        self.input_senha.place(relx=0.25, rely=0.55, relheight=0.15, relwidth=0.5)

        
    def footer(self):
        self.frame_footer = ttk.Frame(self.root)
        self.frame_footer.place(relx=0, rely=0.7, relheight=1, relwidth=1)
        
        self.nome = ttk.Label(self.frame_footer, text="@p._uchoa", font=("Arial", 10, "bold"))
        self.nome.place(relx=0.43,rely=0.2)
        
login()