<<<<<<< HEAD
from tkinter import *
from tkinter import messagebox
from tkinter import ttk # treeview
import os
from Login_with_tkinter import *
from Handle_Shores import *

class application:
    def __init__(self, master=None):
     pass

def ReadFiles(Path):
    file = open(Path,"r",encoding="utf-8")
    texto = file.readlines()
    file.close
    return texto 

def createCategoria(nome):
    file = open("Ficheiros\categorias.txt","a", encoding="utf-8")
    file.write(";" +  nome)
    file.close()

def deleteCategoria(nome):
    texto = ReadFiles("Ficheiros\categorias.txt")
    categorias = str(texto[0]).split(";")
    categorias_second = categorias.copy()
    for i in range(len(categorias_second)):
        if str(categorias_second[i]) == nome:
            categorias.pop(i) 
    texto = ";".join(categorias)
    file = open("Ficheiros\categorias.txt","w",encoding="utf-8")
    file.write(texto)
    file.close()

def Criar_conta_TK():
    CriarWindow = Tk()   # Objeto da classe Toplevel, janela principal
    CriarWindow.title("Criar Conta")
    CriarWindow.resizable(False,False)
    appWidth_Criar = 400                   
    appHeight_Criar = 350 
    screenWidth_Criar = CriarWindow.winfo_screenwidth()
    screenHeight_Criar = CriarWindow.winfo_screenheight()
    x_Criar = (screenWidth_Criar/2) - (appWidth_Criar/2)
    y_Criar = (screenHeight_Criar/2) - (appHeight_Criar/2)
    CriarWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth_Criar, appHeight_Criar, int(x_Criar), int(y_Criar)))
    CriarWindow.focus_force()  # força o focus na window atual
    CriarWindow.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)
    
    # Label
    labelTitulo_Criar = Label(CriarWindow, text ="Criar uma conta",font = ("Helvetica", "20"))
    labelTitulo_Criar.place(x=45, y= 30)
    
    # Username
    labelUsersCriar = Label(CriarWindow, text ="Username:",font = ("Helvetica", "10"))
    labelUsersCriar.place(x=50, y= 98)

    userNameCriar = StringVar()
    txtUserCriar = Entry(CriarWindow, width=25, textvariable=userNameCriar)
    txtUserCriar.place(x=180, y= 100)
    
    #Password
    labelPassCriar = Label(CriarWindow, text ="Password:",font = ("Helvetica", "10"))
    labelPassCriar.place(x=50, y= 148)

    userPassCriar = StringVar()
    txtPassCriar = Entry(CriarWindow, width=25, textvariable = userPassCriar, show = "*")
    txtPassCriar.place(x=180, y= 150)
    
    #PasswordConfirmar
    labelPassCriar_Confirmar = Label(CriarWindow, text ="Confirmar Password:",font = ("Helvetica", "10"))
    labelPassCriar_Confirmar.place(x=50, y= 198)

    userPassCriar_Confirmar = StringVar()
    txtPassCriar_Confirmar = Entry(CriarWindow, width=25, textvariable = userPassCriar_Confirmar, show = "*")
    txtPassCriar_Confirmar.place(x=180, y= 200)

    btnCriarConta= Button(CriarWindow, text = "Criar Conta", width=15, height=2,font = ("Helvetica", "15"),command = lambda: criaConta(txtUserCriar.get(), txtPassCriar.get(), txtPassCriar_Confirmar.get(),CriarWindow))
    btnCriarConta.place(x=110, y= 250) 

def Login_tk():
    
    if userAutenticado.get() != "":     # SE JÁ EXISTE um user autenticado, a ideia é terminar sessão
        if userAutenticado.get() == "Admin":
            btnAdmin.destroy()

        AdminTreeview_info(userAutenticado.get())
        userAutenticado.set("")
        btnVerAtividades.configure(state="disable")
        btnIniciarSessao.config(text = "Iniciar Sessão")
        global btnCriarConta
        btnCriarConta = Button (PanelStatus, image = imageConta,  text = "Criar Conta", width = 95, height = 68, compound=TOP,font = ("Helvetica", "10"), command=Criar_conta_TK)
        btnCriarConta.place(x=960, y=12)
        return

    LogWindow = Tk()   # Objeto da classe Toplevel, janela principal
    LogWindow.title("Login")
    LogWindow.resizable(False,False)
    appWidth_login = 400                   
    appHeight_login = 300  
    screenWidth_login = LogWindow.winfo_screenwidth()
    screenHeight_login = LogWindow.winfo_screenheight()
    x_login = (screenWidth_login/2) - (appWidth_login/2)
    y_login = (screenHeight_login/2) - (appHeight_login/2)
    LogWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth_login, appHeight_login, int(x_login), int(y_login)))
    LogWindow.focus_force()  # força o focus na window atual
    LogWindow.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)


    
    # Label
    labelTitulo_login = Label(LogWindow, text ="Faça Login na sua conta",font = ("Helvetica", "20"))
    labelTitulo_login.place(x=45, y= 30)

    # Username
    labelUsers = Label(LogWindow, text ="Username:",font = ("Helvetica", "10"))
    labelUsers.place(x=50, y= 98)

    userName = StringVar()
    txtUser = Entry(LogWindow, width=35, textvariable=userName)
    txtUser.place(x=120, y= 100)

    #Password
    labelPass = Label(LogWindow, text ="Password:",font = ("Helvetica", "10"))
    labelPass.place(x=50, y= 148)

    userPass = StringVar()
    txtPass = Entry(LogWindow, width=35, textvariable = userPass, show = "*")
    txtPass.place(x=120, y= 150)

    btnValidar= Button(LogWindow, text = "Login", width=15, height=2,font = ("Helvetica", "15"),command = lambda: autenticarUser(txtUser.get(), txtPass.get(), LogWindow))
    btnValidar.place(x=110, y= 200) 
    
def autenticarUser(userName, userPass, Log_window):
    global userAutenticado
    userAutenticado.set(validaConta(userName, userPass, Log_window))
    if userAutenticado.get() != "":
        btnIniciarSessao.config(text = "Terminar Sessão")
        btnVerAtividades.configure(state="active")
        btnCriarConta.destroy()
    if userAutenticado.get() == "Admin":
        global btnAdmin
        btnAdmin = Button(PanelStatus, text = "Admin", width = 11, height = 4,font = ("Helvetica", "10"),command= AdminOpen)
        btnAdmin.place(x=270, y=12)

def AdminOpen():
    window_admin = Tk()
    window_admin.resizable(False,False)
    Admin_screen = window_admin.winfo_screenwidth()
    Admin_heightscreen = window_admin.winfo_screenheight()
    appWidth_admin = 1100                             # tamanho (pixeis) da window a criar 1100 / 700
    appHeight_admin = 700 
    x_admin = (Admin_screen/2) - (appWidth_admin/2)        # posição do canto superior esquerdo da window
    y_admin = (Admin_heightscreen/2) - (appHeight_admin/2)
    window_admin.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth_admin, appHeight_admin, int(x_admin), int(y_admin)))
    window_admin.title('Admin')
    window_admin.focus_force()  # força o focus na window atual
    window_admin.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)
    
    PanelStatus_admin = PanedWindow(window_admin, width=250, height=100, relief="sunken")
    PanelStatus_admin.place(x=10, y=50)

    # Username
    labelUsername = Label(PanelStatus_admin, text ="Username",font = ("Helvetica", "10"))
    labelUsername.place(x=5, y= 12)

    FiltrarUsername = StringVar()
    txtUsername = Entry(PanelStatus_admin, width=25, textvariable=FiltrarUsername)
    txtUsername.place(x=75, y= 15)

    #button Filtrar
    btn_filtrar = Button(PanelStatus_admin, text="Filtrar",font = ("Helvetica", "10"), width=11, height=2,command = lambda: AdminTreeview_insert(txtUsername.get(),tree))
    btn_filtrar.place(x=80, y=45)

    panel_treeview = PanedWindow(window_admin, width = 700, height = 265, bd = "3", relief = "sunken")
    panel_treeview.place(x=350, y=10)

    # TreeView para consulta de movimentos
    tree = ttk.Treeview(panel_treeview, height = 11, selectmode = "browse", columns = ("Username", "Data", "Hora", "Movimento"), show = "headings")
 
    tree.column("Username", width = 160,   anchor="c")
    tree.column("Data", width = 160,  anchor="c")          # c- center, e - direita, w- esquerda
    tree.column("Hora", width = 160,   anchor="c")
    tree.column("Movimento", width = 200,   anchor="c")
    tree.heading("Username", text = "Username")
    tree.heading("Data", text = "Data")
    tree.heading("Hora", text = "Hora")
    tree.heading("Movimento", text = "Movimento")
    tree.place(x=5, y=5)

def FuncaoSair(window):
    if userAutenticado.get() != "":
        AdminTreeview_info(userAutenticado.get())
    window.quit()

def VoltarMenu(window_Tarefas):
    window_Tarefas.destroy()
    window.deiconify()

def updateTreeview(tree,categoria, dataprazo):
    shoresBruto = readShores()
    for i in range(len(shoresBruto)):
        campos = shoresBruto[i].split(";")
        if campos[2] == userAutenticado.get() and categoria == "" and dataprazo == "":
            tree.insert("","end", values = (campos[0],campos[6], campos[3], campos[5],campos[4],campos[7]))
        
def Open_Tarefas():
    window.withdraw()
    Window_Tarefas = Toplevel() #Insere no topo do ecrã 
    Window_Tarefas.title("Tarefas")
    Window_Tarefas.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    Window_Tarefas.focus_force()
    Window_Tarefas.grab_set()
    Window_Tarefas.resizable(False,False)
    Window_Tarefas.overrideredirect(True) 

    barraMenu = Menu(Window_Tarefas)
    barraMenu.add_command(label = "Pagina Principal", command= lambda:VoltarMenu(Window_Tarefas))
    barraMenu.add_command(label = "Gestão User", command= "")
    barraMenu.add_command(label = "Sair", command= Window_Tarefas.quit)
    Window_Tarefas.configure(menu=barraMenu)

    label1 = Label(Window_Tarefas, text="Gestão de tarefas", fg="black", font=("",40))
    label1.place(x = 337, y = 10)

    lFrame = LabelFrame(Window_Tarefas, width = 270, height=300, bd=3, text= "Filtros", fg = "blue", relief = "ridge")
    lFrame.place(x=10, y=75)

    #Filtro categoria
    
    label1 = Label(lFrame, text="Categoria :", fg="black", font=("",10))
    label1.place(x = 10, y = 60)
    
    texto = ReadFiles("Ficheiros\categorias.txt")
    categorias = str(texto[0]).split(";")

    categoria = StringVar()
    drop = ttk.Combobox(lFrame, textvariable= categoria, values= categorias, state="readonly", font=("",10))
    drop.place(x = 80, y = 60)


    #Filtro data prazo

    label2 = Label(lFrame, text="Data Prazo :", fg="black", font=("",10))
    label2.place(x = 10, y = 120)

    DataPrazo=StringVar() #caso queiras escrever algo na entry/ else retira-se o textvariable e a variavel criada por esta linha
    DataPrazo_Entry = Entry(lFrame,width=21, textvariable=DataPrazo, font=("",10))
    DataPrazo_Entry.place(x=90,y=123)

    #Botão filtrar

    button_Filtrar = Button(lFrame,text="Filtrar", width= 20,height=1, font=("",10), bd=2,  command="")
    button_Filtrar.place(x = 50, y = 180)

    #Botão criar
    button_Criar = Button(Window_Tarefas,text="Criar", width= 28,height=2, font=("",12), bd=2,  command=criarTarefa)
    button_Criar.place(x = 15, y = 380)

    #Botão editar
    button_Editar = Button(Window_Tarefas,text="Editar", width= 28,height=2, font=("",12), bd=2,  command="")
    button_Editar.place(x = 15, y = 445)

    #treeview
    
    tree = ttk.Treeview(Window_Tarefas, height = 20, selectmode = "browse", columns = ("id","Titulo", "Estado", "Categoria","DataPrazo", "Conteudo"), show = "headings")

    tree.column("id", stretch=NO, minwidth=0, width=0,   anchor="c")
    tree.column("Titulo", width = 200,   anchor="c")
    tree.column("Estado", width = 100,  anchor="c") 
    tree.column("Categoria", width = 150,   anchor="c")
    tree.column("DataPrazo", width = 150,  anchor="c") 
    tree.column("Conteudo", width = 200,   anchor="c")
    tree.heading("id", text = "")
    tree.heading("Titulo", text = "Titulo")
    tree.heading("Estado", text = "Estado")
    tree.heading("Categoria", text = "Categoria")
    tree.heading("DataPrazo", text = "DataPrazo")
    tree.heading("Conteudo", text = "Conteudo")
    tree.place(x = 285, y = 81)

    updateTreeview(tree, categoria.get(), DataPrazo.get())

def criarTarefa():
    window_criacao = Toplevel() #Insere no topo do ecrã 
    window_criacao.title("Tarefas")
    x2 = (screenWidth/2) - (550/2)        # posição do canto superior esquerdo da window
    y2 = (screenHeight/2) - (300/2)
    window_criacao.geometry(f'{550}x{300}+{int(x2)}+{int(y2)}')
    window_criacao.focus_force()
    window_criacao.grab_set()
    window_criacao.resizable(False,False) 
    window_criacao.title('Criação de tarefa')
    window_criacao.config(bg='#87CEFA')


    #Label 
    lbltitulo= Label(window_criacao, text = "TITULO",bg='#87CEFA', font=("helvetica", 8))
    lbltitulo.place(x=7, y=60)

    lbldatapz= Label(window_criacao,text= "DATA PRAZO",bg='#87CEFA', font=("helvetica", 8))
    lbldatapz.place(x=7,y=275)

    lbluser= Label(window_criacao,text= "USER",bg='#87CEFA', font=("helvetica", 8))
    lbluser.place(x=505, y=10)

    lblcomentario= Label(window_criacao,text= "CONTEUDO",bg='#87CEFA', font=("helvetica", 8))
    lblcomentario.place(x=7, y=110)

    lblcategorias= Label(window_criacao,text= "CATEGORIAS",bg='#87CEFA', font=("helvetica", 8))
    lblcategorias.place(x=8, y=10)

    #Box
    texto = ReadFiles("Ficheiros\categorias.txt")
    categorias = str(texto[0]).split(";")
    categoria = StringVar()
    categorias = ttk.Combobox(window_criacao, values=categorias, state="readonly",textvariable=categoria)
    categorias.place(x=10, y=30)

    titulo = StringVar()
    txttitulo = Entry(window_criacao, width=88, textvariable=titulo)
    txttitulo.place(x=10, y=80)

    txtmain = Text(window_criacao, width=66, height = 6)
    txtmain.place(x=10, y=130)

    dataprazo = StringVar
    txtdatapz = Entry(window_criacao, width=20, textvariable= dataprazo)
    txtdatapz.place(x=10, y=250)

    #dropdownlist
    global listaUsers 
    listaUsers= []
    TextoCategorias = ReadFiles("Ficheiros\dados.txt")
    for i in TextoCategorias:
        listaUsers.append(str(i).split(";")[0])

    userCriacao =StringVar()
    user = ttk.Combobox(window_criacao, values=listaUsers,state="readonly", textvariable = userCriacao )
    user.place(x=399, y=30)
    
    #Button
    btn=Button(window_criacao, width=20, text="CRIAR TAREFA", command= lambda: insertTarefa(user.get(),categorias.get(),txttitulo.get(), txtmain.get(1.0,END),"Iniciada",txtdatapz.get()))
    btn.place(x=395, y=245)



window = Tk()
window.resizable(False,False)
window.overrideredirect(True) 
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1100                             # tamanho (pixeis) da window a criar 1100 / 700
appHeight = 600 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Gestor de Tarefas')

PanelStatus = PanedWindow(window, width=1100, height=100, relief = "sunken")
PanelStatus.place(x=0, y=0)

btnVerAtividades = Button(PanelStatus, text = "Ver Atividades", width = 11, height = 4,font = ("Helvetica", "10"), state="disable", command=Open_Tarefas)
btnVerAtividades.place(x=50, y=12)

btnSair = Button(PanelStatus, text = "Sair", width = 11, height = 4,font = ("Helvetica", "10"), command = lambda: FuncaoSair(window))
btnSair.place(x=160, y=12)

global btnIniciarSessao
imageLogin = PhotoImage(file = "imagens\\icoLogin.png")
btnIniciarSessao = Button (PanelStatus, image = imageLogin, text = "Iniciar Sessão", width = 95, height = 68, compound=TOP,font = ("Helvetica", "10"), command=Login_tk)
btnIniciarSessao.place(x=850, y=12)

global btnCriarConta
imageConta = PhotoImage(file = "imagens\\icoConta.png" )
btnCriarConta = Button (PanelStatus, image = imageConta,  text = "Criar Conta", width = 95, height = 68, compound=TOP,font = ("Helvetica", "10"), command=Criar_conta_TK)
btnCriarConta.place(x=960, y=12)

global userAutenticado
userAutenticado = StringVar()
userAutenticado.set("")
labelHeader = Label(PanelStatus, textvariable= userAutenticado, fg = "red", font=("Helvetica", "20"))
labelHeader.place(x= 960, y= 32)

panel2 = PanedWindow(window, width=1100, height=600)
panel2.place(x=0, y=98)

ctnCanvas = Canvas(panel2, width = 1100, height= 600)
ctnCanvas.place(x=0, y= 0)

global img
img = PhotoImage(file = ".\imagens\\1100x600.png")
ctnCanvas.create_image(550, 300, image = img)

window.mainloop()
=======
from tkinter import *
from tkinter import messagebox
from tkinter import ttk # treeview
import os
from Login_with_tkinter import *
from Handle_Shores import *

class application:
    def __init__(self, master=None):
     pass

def Criar_conta_TK():
    CriarWindow = Tk()   # Objeto da classe Toplevel, janela principal
    CriarWindow.title("Criar Conta")
    CriarWindow.resizable(False,False)
    appWidth_Criar = 400                   
    appHeight_Criar = 350 
    screenWidth_Criar = CriarWindow.winfo_screenwidth()
    screenHeight_Criar = CriarWindow.winfo_screenheight()
    x_Criar = (screenWidth_Criar/2) - (appWidth_Criar/2)
    y_Criar = (screenHeight_Criar/2) - (appHeight_Criar/2)
    CriarWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth_Criar, appHeight_Criar, int(x_Criar), int(y_Criar)))
    CriarWindow.focus_force()  # força o focus na window atual
    CriarWindow.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)
    
    # Label
    labelTitulo_Criar = Label(CriarWindow, text ="Criar uma conta",font = ("Helvetica", "20"))
    labelTitulo_Criar.place(x=45, y= 30)
    
    # Username
    labelUsersCriar = Label(CriarWindow, text ="Username:",font = ("Helvetica", "10"))
    labelUsersCriar.place(x=50, y= 98)

    userNameCriar = StringVar()
    txtUserCriar = Entry(CriarWindow, width=25, textvariable=userNameCriar)
    txtUserCriar.place(x=180, y= 100)
    
    #Password
    labelPassCriar = Label(CriarWindow, text ="Password:",font = ("Helvetica", "10"))
    labelPassCriar.place(x=50, y= 148)

    userPassCriar = StringVar()
    txtPassCriar = Entry(CriarWindow, width=25, textvariable = userPassCriar, show = "*")
    txtPassCriar.place(x=180, y= 150)
    
    #PasswordConfirmar
    labelPassCriar_Confirmar = Label(CriarWindow, text ="Confirmar Password:",font = ("Helvetica", "10"))
    labelPassCriar_Confirmar.place(x=50, y= 198)

    userPassCriar_Confirmar = StringVar()
    txtPassCriar_Confirmar = Entry(CriarWindow, width=25, textvariable = userPassCriar_Confirmar, show = "*")
    txtPassCriar_Confirmar.place(x=180, y= 200)

    btnCriarConta= Button(CriarWindow, text = "Criar Conta", width=15, height=2,font = ("Helvetica", "15"),command = lambda: criaConta(txtUserCriar.get(), txtPassCriar.get(), txtPassCriar_Confirmar.get(),CriarWindow))
    btnCriarConta.place(x=110, y= 250) 

def Login_tk():
    
    if userAutenticado.get() != "":     # SE JÁ EXISTE um user autenticado, a ideia é terminar sessão
        if userAutenticado.get() == "Admin":
            btnAdmin.destroy()

        AdminTreeview_info(userAutenticado.get())
        userAutenticado.set("")
        btnVerAtividades.configure(state="disable")
        btnIniciarSessao.config(text = "Iniciar Sessão")
        global btnCriarConta
        btnCriarConta = Button (PanelStatus, image = imageConta,  text = "Criar Conta", width = 95, height = 68, compound=TOP,font = ("Helvetica", "10"), command=Criar_conta_TK)
        btnCriarConta.place(x=960, y=12)
        return

    LogWindow = Tk()   # Objeto da classe Toplevel, janela principal
    LogWindow.title("Login")
    LogWindow.resizable(False,False)
    appWidth_login = 400                   
    appHeight_login = 300  
    screenWidth_login = LogWindow.winfo_screenwidth()
    screenHeight_login = LogWindow.winfo_screenheight()
    x_login = (screenWidth_login/2) - (appWidth_login/2)
    y_login = (screenHeight_login/2) - (appHeight_login/2)
    LogWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth_login, appHeight_login, int(x_login), int(y_login)))
    LogWindow.focus_force()  # força o focus na window atual
    LogWindow.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)


    
    # Label
    labelTitulo_login = Label(LogWindow, text ="Faça Login na sua conta",font = ("Helvetica", "20"))
    labelTitulo_login.place(x=45, y= 30)

    # Username
    labelUsers = Label(LogWindow, text ="Username:",font = ("Helvetica", "10"))
    labelUsers.place(x=50, y= 98)

    userName = StringVar()
    txtUser = Entry(LogWindow, width=35, textvariable=userName)
    txtUser.place(x=120, y= 100)

    #Password
    labelPass = Label(LogWindow, text ="Password:",font = ("Helvetica", "10"))
    labelPass.place(x=50, y= 148)

    userPass = StringVar()
    txtPass = Entry(LogWindow, width=35, textvariable = userPass, show = "*")
    txtPass.place(x=120, y= 150)

    btnValidar= Button(LogWindow, text = "Login", width=15, height=2,font = ("Helvetica", "15"),command = lambda: autenticarUser(txtUser.get(), txtPass.get(), LogWindow))
    btnValidar.place(x=110, y= 200) 
    
def autenticarUser(userName, userPass, Log_window):
    global userAutenticado
    userAutenticado.set(validaConta(userName, userPass, Log_window))
    if userAutenticado.get() != "":
        btnIniciarSessao.config(text = "Terminar Sessão")
        btnVerAtividades.configure(state="active")
        btnCriarConta.destroy()
    if userAutenticado.get() == "Admin":
        global btnAdmin
        btnAdmin = Button(PanelStatus, text = "Admin", width = 11, height = 4,font = ("Helvetica", "10"),command= AdminOpen)
        btnAdmin.place(x=270, y=12)

def AdminOpen():
    window_admin = Tk()
    window_admin.resizable(False,False)
    Admin_screen = window_admin.winfo_screenwidth()
    Admin_heightscreen = window_admin.winfo_screenheight()
    appWidth_admin = 1100                             # tamanho (pixeis) da window a criar 1100 / 700
    appHeight_admin = 700 
    x_admin = (Admin_screen/2) - (appWidth_admin/2)        # posição do canto superior esquerdo da window
    y_admin = (Admin_heightscreen/2) - (appHeight_admin/2)
    window_admin.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth_admin, appHeight_admin, int(x_admin), int(y_admin)))
    window_admin.title('Admin')
    window_admin.focus_force()  # força o focus na window atual
    window_admin.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)
    
    PanelStatus_admin = PanedWindow(window_admin, width=250, height=100, relief="sunken")
    PanelStatus_admin.place(x=10, y=50)

    # Username
    labelUsername = Label(PanelStatus_admin, text ="Username",font = ("Helvetica", "10"))
    labelUsername.place(x=5, y= 12)

    FiltrarUsername = StringVar()
    txtUsername = Entry(PanelStatus_admin, width=25, textvariable=FiltrarUsername)
    txtUsername.place(x=75, y= 15)

    #button Filtrar
    btn_filtrar = Button(PanelStatus_admin, text="Filtrar",font = ("Helvetica", "10"), width=11, height=2,command = lambda: AdminTreeview_insert(txtUsername.get(),tree))
    btn_filtrar.place(x=80, y=45)

    panel_treeview = PanedWindow(window_admin, width = 700, height = 265, bd = "3", relief = "sunken")
    panel_treeview.place(x=350, y=10)

    # TreeView para consulta de movimentos
    tree = ttk.Treeview(panel_treeview, height = 11, selectmode = "browse", columns = ("Username", "Data", "Hora", "Movimento"), show = "headings")
 
    tree.column("Username", width = 160,   anchor="c")
    tree.column("Data", width = 160,  anchor="c")          # c- center, e - direita, w- esquerda
    tree.column("Hora", width = 160,   anchor="c")
    tree.column("Movimento", width = 200,   anchor="c")
    tree.heading("Username", text = "Username")
    tree.heading("Data", text = "Data")
    tree.heading("Hora", text = "Hora")
    tree.heading("Movimento", text = "Movimento")
    tree.place(x=5, y=5)

def FuncaoSair(window):
    if userAutenticado.get() != "":
        AdminTreeview_info(userAutenticado.get())
    window.quit()

def VoltarMenu(window_Tarefas):
    window_Tarefas.destroy()
    window.deiconify()

def Open_Tarefas():
    window.withdraw()
    Window_Tarefas = Toplevel() #Insere no topo do ecrã 
    Window_Tarefas.title("Tarefas")
    Window_Tarefas.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    Window_Tarefas.focus_force()
    Window_Tarefas.grab_set()
    Window_Tarefas.resizable(False,False)
    Window_Tarefas.overrideredirect(True) 

    barraMenu = Menu(Window_Tarefas)
    barraMenu.add_command(label = "Pagina Principal", command= lambda:VoltarMenu(Window_Tarefas))
    barraMenu.add_command(label = "Gestão User", command= "")
    barraMenu.add_command(label = "Sair", command= Window_Tarefas.quit)
    Window_Tarefas.configure(menu=barraMenu)

    label1 = Label(Window_Tarefas, text="Gestão de tarefas", fg="black", font=("",40))
    label1.place(x = 337, y = 10)

    lFrame = LabelFrame(Window_Tarefas, width = 270, height=300, bd=3, text= "Filtros", fg = "blue", relief = "ridge")
    lFrame.place(x=10, y=75)

    #Filtro categoria
    
    label1 = Label(lFrame, text="Categoria :", fg="black", font=("",10))
    label1.place(x = 10, y = 60)
    
    categoria = StringVar()
    drop = ttk.Combobox(lFrame, textvariable= categoria, values= "", state="readonly", font=("",10))
    drop.place(x = 80, y = 60)


    #Filtro data prazo

    label2 = Label(lFrame, text="Data Prazo :", fg="black", font=("",10))
    label2.place(x = 10, y = 120)

    DataPrazo=StringVar() #caso queiras escrever algo na entry/ else retira-se o textvariable e a variavel criada por esta linha
    DataPrazo_Entry = Entry(lFrame,width=21, textvariable=DataPrazo, font=("",10))
    DataPrazo_Entry.place(x=90,y=123)

    #Botão filtrar

    button_Filtrar = Button(lFrame,text="Filtrar", width= 20,height=1, font=("",10), bd=2,  command="")
    button_Filtrar.place(x = 50, y = 180)

    #Botão criar
    button_Criar = Button(Window_Tarefas,text="Criar", width= 28,height=2, font=("",12), bd=2,  command=criarTarefa)
    button_Criar.place(x = 15, y = 380)

    #Botão editar
    button_Editar = Button(Window_Tarefas,text="Editar", width= 28,height=2, font=("",12), bd=2,  command="")
    button_Editar.place(x = 15, y = 445)

    #treeview
    
    tree = ttk.Treeview(Window_Tarefas, height = 20, selectmode = "browse", columns = ("Titulo", "Estado", "Categoria","DataPrazo", "Conteudo"), show = "headings")

    tree.column("Titulo", width = 200,   anchor="c")
    tree.column("Estado", width = 100,  anchor="c") 
    tree.column("Categoria", width = 150,   anchor="c")
    tree.column("DataPrazo", width = 150,  anchor="c") 
    tree.column("Conteudo", width = 200,   anchor="c")
    tree.heading("Titulo", text = "Titulo")
    tree.heading("Estado", text = "Estado")
    tree.heading("Categoria", text = "Categoria")
    tree.heading("DataPrazo", text = "DataPrazo")
    tree.heading("Conteudo", text = "Conteudo")
    tree.place(x = 285, y = 81)

def criarTarefa():
    window_criacao = Toplevel() #Insere no topo do ecrã 
    window_criacao.title("Tarefas")
    x2 = (screenWidth/2) - (550/2)        # posição do canto superior esquerdo da window
    y2 = (screenHeight/2) - (300/2)
    window_criacao.geometry(f'{550}x{300}+{int(x2)}+{int(y2)}')
    window_criacao.focus_force()
    window_criacao.grab_set()
    window_criacao.resizable(False,False)
    window_criacao.overrideredirect(True) 
    window_criacao.title('Criação de tarefa')
    window_criacao.config(bg='#87CEFA')


    #Label 
    lbltitulo= Label(window_criacao, text = "TITULO",bg='#87CEFA', font=("helvetica", 8))
    lbltitulo.place(x=7, y=60)

    lbldatapz= Label(window_criacao,text= "DATA PRAZO",bg='#87CEFA', font=("helvetica", 8))
    lbldatapz.place(x=7,y=275)

    lbluser= Label(window_criacao,text= "USER",bg='#87CEFA', font=("helvetica", 8))
    lbluser.place(x=505, y=10)

    lblcomentario= Label(window_criacao,text= "COMENTARIO",bg='#87CEFA', font=("helvetica", 8))
    lblcomentario.place(x=7, y=110)

    lblcategorias= Label(window_criacao,text= "CATEGORIAS",bg='#87CEFA', font=("helvetica", 8))
    lblcategorias.place(x=8, y=10)

    #Box
    txtcategorias = Entry(window_criacao, width=20)
    txtcategorias.place(x=10, y=30)

    txtconteudo = Entry(window_criacao, width=88)
    txtconteudo.place(x=10, y=80)

    txtmain = Text(window_criacao, width=66, height = 6)
    txtmain.place(x=10, y=130)

    txtdatapz = Entry(window_criacao, width=20)
    txtdatapz.place(x=10, y=250)

    #Button
    btn=Button(window_criacao, width=20, text="CRIAR TAREFA")
    btn.place(x=395, y=245)

    #dropdownlist
    lista = []
    user = ttk.Combobox(window_criacao, values=lista)
    user.place(x=399, y=30)



window = Tk()
window.resizable(False,False)
window.overrideredirect(True) 
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1100                             # tamanho (pixeis) da window a criar 1100 / 700
appHeight = 600 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Gestor de Tarefas')

PanelStatus = PanedWindow(window, width=1100, height=100, relief = "sunken")
PanelStatus.place(x=0, y=0)

btnVerAtividades = Button(PanelStatus, text = "Ver Atividades", width = 11, height = 4,font = ("Helvetica", "10"), state="disable", command=Open_Tarefas)
btnVerAtividades.place(x=50, y=12)

btnSair = Button(PanelStatus, text = "Sair", width = 11, height = 4,font = ("Helvetica", "10"), command = lambda: FuncaoSair(window))
btnSair.place(x=160, y=12)

global btnIniciarSessao
imageLogin = PhotoImage(file = "imagens\\icoLogin.png")
btnIniciarSessao = Button (PanelStatus, image = imageLogin, text = "Iniciar Sessão", width = 95, height = 68, compound=TOP,font = ("Helvetica", "10"), command=Login_tk)
btnIniciarSessao.place(x=850, y=12)

global btnCriarConta
imageConta = PhotoImage(file = "imagens\\icoConta.png" )
btnCriarConta = Button (PanelStatus, image = imageConta,  text = "Criar Conta", width = 95, height = 68, compound=TOP,font = ("Helvetica", "10"), command=Criar_conta_TK)
btnCriarConta.place(x=960, y=12)

global userAutenticado
userAutenticado = StringVar()
userAutenticado.set("")
labelHeader = Label(PanelStatus, textvariable= userAutenticado, fg = "red", font=("Helvetica", "20"))
labelHeader.place(x= 960, y= 32)

panel2 = PanedWindow(window, width=1100, height=600)
panel2.place(x=0, y=98)

ctnCanvas = Canvas(panel2, width = 1100, height= 600)
ctnCanvas.place(x=0, y= 0)

global img
img = PhotoImage(file = ".\imagens\\1100x600.png")
ctnCanvas.create_image(550, 300, image = img)

window.mainloop()
>>>>>>> 0ad221c1f65e1137507892a174d47e73593442cb
