"""
Este ficheiro tem como principal propósito trabalhar sobre as tarefas
Faz hadling de:
    -Inserção
    -Eliminação
    -Edição
tem também algumas funções de apoio com ficheiros como leitura, criação etc
"""
import os
from datetime import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



path = "Ficheiros\\Shores.txt"

def readShores():
    """
    Função que faz a leitura do ficheiro de tarefas
    Devolve um array com as tarefas separadas
    """
    file = open(path,"r", encoding="utf-8")
    textolist = file.readlines()
    file.close()
    return textolist

def checkDirectorie():
    """
    Função verifica se o ficheiro dado existe bem como o caminho da pasta anterior ao ficheiro
    Devolve o ficheiro criado bem como a pasta
    Input: Path(str)
    """

    path_folder = path.rsplit(os.sep, 1)[0] + os.sep   #Separa o path dos folders do ficheiro para verificação
    if not(os.path.exists(path_folder)):
        os.mkdir(path_folder)
    if not(os.path.isfile(path)):
        file = open(path,"x", encoding="utf-8")
        file.close()

def insertTarefa(user,categoria,titulo,conteudo,estado,data_Prazo,window2, windowMain):
    """
    Função que insere as tarefas no ficheiro das Shores
    """
    #Verifica o conteudo das variaveis
    if user == "" or categoria == "" or titulo == "" or conteudo == "" or data_Prazo == "":
        messagebox.showwarning(title="Campos vazios", message="Não preencheu devidamente os campos da tarefa. Um ou mais encontram-se vazios")  #Warning
        return 0
    
    data_Prazo = data_Prazo.replace("/","-")
    data_Prazo = data_Prazo.replace(".","-")
    try:
        dataComp = datetime.strptime(data_Prazo, "%d-%m-%Y")
    except:
        messagebox.showwarning(title="Erro ao inserir a data", message="Não inseriu a data corretamente. Deve inserir o dia(dd) de seguida o mes(mm) e de seguida o ano(yyyy)")
        return 0
    
    if dataComp.date() >= (datetime.strptime((datetime.now()).strftime("%d-%m-%Y"),"%d-%m-%Y")).date():
        data_Prazo = str((dataComp).strftime("%d-%m-%Y %H:%M:%S")).split(" ")[0]
    else:
        messagebox.showwarning(title="Erro ao inserir a data", message="Escreva uma data maior que o dia de hoje")
        return 0

     


    #calculo de id consoante a ultima tarefa
    shores = readShores()
    shores.reverse()
    campos = shores[0].split(";")
    if campos[0] == "":
        id = 1
    else:
        id = int(campos[0]) + 1

    #Criação da linha a inserir
    conteudo.strip()
    conteudo = "(/)".join(conteudo.splitlines())
    texto =str(id) + ";" + str((datetime.now()).strftime("%d-%m-%Y %H:%M:%S")) + ";" + user +";" + estado + ";" + str(data_Prazo) + ";"  + categoria + ";" + titulo + ";" + conteudo + "\n"
    
    #Escrita da tarefa
    checkDirectorie()
    file = open(path,"a", encoding="utf-8")
    file.write(texto)
    file.close()

    messagebox.showinfo(title="Sucesso", message="A tarefa foi adicionada")
    window2.withdraw()
    windowMain.focus_force()
    windowMain.grab_set()

def eliminateTarefa(user,titulo,dataprazo,window):
    shores = readShores()
    texto = ""
    linha = ""
    ask = messagebox.askokcancel("Atividade", "Tem a certeza que quer alterar a atividade?")
    if ask == True:
        for i in range(len(shores)):
            campos = shores[i].split(";")
            if not (user == str(campos[2]) and titulo == str(campos[6]) and dataprazo == str(campos[4])):
                linha = ";".join(campos)
                texto += linha


        file = open(path,"w", encoding="utf-8")
        file.write(texto)
        file.close()
        window.destroy()

def Editar_Atividade(Linha_nonEdited, titulo,estado,categoria,conteudo,data_Prazo,Window_edit):
    """
    Função que insere as tarefas no ficheiro das Shores
    """
    #Verifica o conteudo das variaveis
    user = Linha_nonEdited.split(";")[2]
    if user == "" or categoria == "" or titulo == "" or conteudo == "" or data_Prazo == "":
        messagebox.showwarning(title="Campos vazios", message="Não preencheu devidamente os campos da tarefa. Um ou mais encontram-se vazios")  #Warning
        return 0
    
    data_Prazo = data_Prazo.replace("/","-")
    data_Prazo = data_Prazo.replace(".","-")
    try:
        dataComp = datetime.strptime(data_Prazo, "%d-%m-%Y")
    except:
        messagebox.showwarning(title="Erro ao inserir a data", message="Não inseriu a data corretamente. Deve inserir o dia(dd) de seguida o mes(mm) e de seguida o ano(yyyy)")
        return 0
    
    if dataComp.date() >= (datetime.strptime((datetime.now()).strftime("%d-%m-%Y"),"%d-%m-%Y")).date():
        data_Prazo = str((dataComp).strftime("%d-%m-%Y %H:%M:%S")).split(" ")[0]
    else:
        messagebox.showwarning(title="Erro ao inserir a data", message="Escreva uma data maior que o dia de hoje")
        return 0

    #Criação da linha a inserir
    conteudo.strip()
    conteudo = "(/)".join(conteudo.splitlines())
    texto =Linha_nonEdited.split(";")[0] + ";" + str((datetime.now()).strftime("%d-%m-%Y %H:%M:%S")) + ";" + user +";" + estado + ";" + str(data_Prazo) + ";"  + categoria + ";" + titulo + ";" + conteudo + "\n"
    eliminateTarefa(user,Linha_nonEdited.split(";")[6],Linha_nonEdited.split(";")[4],Window_edit)
    
    #Escrita da tarefa
    checkDirectorie()
    file = open(path,"a", encoding="utf-8")
    file.write(texto)
    file.close()

    messagebox.showinfo(title="Sucesso", message="A tarefa foi editada")
    Window_edit.destroy()
    