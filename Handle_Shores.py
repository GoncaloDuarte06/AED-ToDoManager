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


path = "Txt Files\\Shores.txt"

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


def insert(user,categoria,titulo,conteudo,estado, data_Prazo):
    """
    Função que insere as tarefas no ficheiro das Shores
    """
    
    #calculo de id consoante a ultima tarefa
    shores = readShores()
    shores.reverse()
    campos = shores[0].split(";")
    id = int(campos[0]) + 1

    #Criação da linha a inserir
    conteudo.replace("\n","(\)")
    texto =str(id) + ";" + str((datetime.now()).strftime("%d-%m-%Y %H:%M:%S")) + ";" + user +";" + estado + ";" + data_Prazo + ";"  + categoria + ";" + titulo + ";" + conteudo + "\n"
    
    #Escrita da tarefa
    checkDirectorie()
    file = open(path,"a", encoding="utf-8")
    file.write(texto)
    file.close()


def eliminate(user,titulo,data_hora):
    shores = readShores()
    texto = ""
    linha = ""
    for i in range(len(shores)):
        campos = shores[i].split(";")
        if not (user == str(campos[1]) and titulo == str(campos[4]) and data_hora == str(campos[0])):
            linha = ";".join(campos)
            texto += linha


    file = open(path,"w", encoding="utf-8")
    file.write(texto)
    file.close()

