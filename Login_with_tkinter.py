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

def validaConta(userName, userPass, Logwindow):
    """
    Validar cautenticação com uma conta
    """
    fileUsers=open(Ficheiro, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    fileUsers.close()
    for linha in listaUsers:
        if linha.split(";")[0] == userName and linha.split(";")[1] == userPass:
            msg = "Bem-Vindo " + userName
            Admin_info(userName)
            messagebox.showinfo("Iniciar Sessão", msg)
            msg = userName
            Logwindow.destroy()
            return msg
    messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")
    Logwindow.destroy()
    return ""
def Id_conta():
    """
    Verifica o maior id
    """
    fileUsers=open(Ficheiro, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    fileUsers.close()
    ultimo = 0
    for linha in listaUsers:
        if linha != "\n":
            linha.replace("\n","")
            linha = linha.split(";")
            ultimo=int(linha[2])
    ultimo +=1
    ultimo = str(ultimo)
    return ultimo


 


def criaConta(userName, userPass,userPassConfirm, panelUsers):
    """
    Criar uma nova conta
    """
    if userPass != userPassConfirm:
        messagebox.showerror("Criar Conta", "A password difere do inserido na sua confirmação!")
        panelUsers.destroy()
        return  
    if userName == "" or userPass == "":
        messagebox.showerror("Criar Conta", "O username e a password não podem ser vazios!")
        panelUsers.destroy()
        return         
    fileUsers=open(Ficheiro, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    for i in range(len(userName)):
        if userName[i]in ";:/!=-*":
            messagebox.showerror("Criar Conta", "O username esta a utilizar valores invalidos, neste caso foi a letra" + userName[i])
            panelUsers.destroy()
            return         
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == userName:
            messagebox.showerror("Criar Conta", "Já existe um utilizador com esse username!")
            panelUsers.destroy()
            return 
    panelUsers.destroy()    
    fileUsers.close()
    Id=Id_conta()
    fileUsers = open(Ficheiro, "a")
    linha = userName + ";" + userPass + ";" + Id + "\n"
    fileUsers.write(linha)
    fileUsers.close()
    messagebox.showinfo("Criar Conta", "Conta criada com sucesso!")

def Admin_info(userName):
    """
    Guardar informação das horas e id do utilizador para o admin
    """
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    estado = "Entrada"
    admin_linha = userName + ";" + str(today) + ";" + str(current_time) + ";" + estado + "\n"
    f = open(Admin_Ficheiro, "a")
    f.write(admin_linha)
    f.close
    return

def AdminTreeview_info(Username):
    """
    Guardar informação das horas e id do utilizador para o admin
    """
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    estado = "Saida"
    admin_linha = Username + ";" + str(today) + ";" + str(current_time) + ";" + estado + "\n"
    f = open(Admin_Ficheiro, "a")
    f.write(admin_linha)
    f.close
    return
def AdminTreeview_insert(Username, Tree):
    """
    Consulta movimentos em Treeview, de acordo com filtros selecionados
    """
    Tree.delete(*Tree.get_children()) 
    f = open(Admin_Ficheiro, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for linha in lista:
        campos = linha.split(";")
        if Username == "" or Username == campos[0]:
            Tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))