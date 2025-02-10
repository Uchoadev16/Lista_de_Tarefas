from app.index import index
from app.views.login import login
from app.views.cadastro import cadastro
from app.controllers.controller_login import autenticar

if __name__ == "__main__":
    index1 = index()
    login1 = login()
    cadastro1 = cadastro()
    autenticar(index1, login1, cadastro1)