import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from .index import index
from .cadastro import cadastro
from .login import login
from . root import root

class view:
    
    def __init__(self):
        
        root()      
        index()