from tkinter import *
from tkinter import messagebox
import os
from datetime import datetime
from datetime import date


# Funções relacionadas com o User
# Registar, Iniciar Sessão
Pasta = "Ficheiros"
Ficheiro = "Ficheiros\dados.txt"
Admin_Ficheiro = "Ficheiros\_admin.txt"
if not os.path.exists(Pasta):
    os.mkdir(Pasta)

def validaConta(userName, userPass):
    """
    Validar cautenticação com uma conta
    """
    fileUsers=open(Ficheiro, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()    
    for linha in listaUsers:
        if linha.split(";")[0] == userName and linha.split(";")[1][:-1] == userPass:
            msg = "Bem-Vindo " + userName
            messagebox.showinfo("Iniciar Sessão", msg)
            id=linha.split(";")[2]
            Admin_info(userName, id)
            return msg
    fileUsers.close()
    messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")
    return ""
def Id_conta():
    """
    Verifica o maior id
    """
    fileUsers=open(Ficheiro, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    for linha in listaUsers:
        linha = linha.split(";")
        ultimo=int(linha[2])
    ultimo +=1
    ultimo = str(ultimo)
    fileUsers.close()
    return ultimo


 


def criaConta(userName, userPass, panelUsers):
    """
    Criar uma niova conta
    """
   
    if userName == "" or userPass == "":
        messagebox.showerror("Criar Conta", "O username e a password não podem ser vazios!")
        return         
    fileUsers=open(Ficheiro, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    for i in range(len(userName)):
        if userName[i] == ";" or userName[i] == ":" or userName[i] == "/" or userName[i] == "\ " or userName[i] == "?" or userName[i] == "!" or userName[i] == "="or userName[i] == "+"or userName[i] == "-"or userName[i] == "*":
            messagebox.showerror("Criar Conta", "O username esta a utilizar valores invalidos, neste caso foi a letra" + userName[i])
            return         
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == userName:
            messagebox.showerror("Criar Conta", "Já existe um utilizador com esse username!")
            return 
    fileUsers.close()
    Id=Id_conta()
    fileUsers = open(Ficheiro, "a")
    linha = userName + ";" + userPass + ";" + Id + "\n"
    fileUsers.write(linha)
    fileUsers.close()
    messagebox.showinfo("Criar Conta", "Conta criada com sucesso!")
    panelUsers.place_forget()

def Admin_info(userName, id):
    """
    Guardar informação das horas e id do utilizador para o admin
    """
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    linha = userName + ";" + str(today) + ";" + str(current_time) + ";" + id + "\n"
    f = open(Admin_Ficheiro, "a")
    f.write(linha)
    f.close
    return