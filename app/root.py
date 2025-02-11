import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class root:
    root = ttk.Window("Lista de tarefas", themename="superhero")
    
    def __init__(self):
        self.root.iconbitmap("app/img/icone.ico")
        self.root.geometry("550x700")
        self.root.resizable(True, True)
        self.root.maxsize(width=550, height=700)
        self.root.minsize(width=550, height=700)
        self.root.mainloop()