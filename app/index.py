#tkinter
from tkinter import *
from tkinter import Image
from tkinter import ttk

#SqLite
import sqlite3


#class
class index():
    #atributos
    root = Tk()
    
    #construtor
    def __init__(self):
        
        self.tela()
        self.root.mainloop()
    

    #metodos
    def tela(self):
        
        self.root.title("Lista de Tarefas")
        self.root.iconbitmap("app/assets/img/icone.ico")
        self.root.configure(background="#010409")
        self.root.geometry("450x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=450, height=600)
        self.root.minsize(width=450, height=600)
        

index()
    