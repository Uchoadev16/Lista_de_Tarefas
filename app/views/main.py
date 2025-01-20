from tkinter import Tk
from reportlab.pdfgen import canvas

class main():
    #atributos
    root = Tk()

    #construtor
    def __init__(self):
        
        self.tela()
        self.root.mainloop()

    #metodos
    def tela(self):
        
        self.root.title("Lista de Tarefas")
        self.root.configure(background="#010409")

main()
    