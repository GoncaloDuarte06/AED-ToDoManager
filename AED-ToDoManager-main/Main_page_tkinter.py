from tkinter import *
from tkinter import messagebox
from tkinter import ttk # treeview
from datetime import date
import os
from Login_with_tkinter import *
from Handle_Shores import *
options = []

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
    labelTitulo_Criar.place(x=95, y= 30)
    
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
        btnNotificacoes.destroy()
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
        global btnNotificacoes
        btnNotificacoes = Button(ctnCanvas, image= imagemNoti, width = 48, height = 48, command= lambda: Noti_criar(userAutenticado.get()))
        btnNotificacoes.place(x=30, y=420)
    if userAutenticado.get() == "Admin":
        global btnAdmin
        btnAdmin = Button(PanelStatus, text = "Admin", width = 11, height = 4,font = ("Helvetica", "10"),command= AdminOpen)
        btnAdmin.place(x=270, y=12)

def Categoria_Optionsadmin(Categoria):
    global options
    options=[]
    options=Adicionar_Categorias(Categoria)
    dropdown_admin['values'] = options

def Categoria_Removeadmin(Categoria):
    global options
    options=[]
    options=Remover_Categorias(Categoria)
    dropdown_admin['values'] = options

def AdminOpen():
    window.withdraw()
    window_admin = Toplevel() #Insere no topo do ecrã 
    window_admin.title('Admin')                          
    appHeight_admin = 365 
    y_admin = (screenHeight/2) - (appHeight_admin/2)
    window_admin.geometry(f'{appWidth}x{appHeight_admin}+{int(x)}+{int(y_admin)}')
    window_admin.focus_force()
    window_admin.grab_set()
    window_admin.resizable(False,False)
    window_admin.overrideredirect(True) 
    
    labelAdmin = Label(window_admin, text ="Gestor da Aplicação do Admin",font = ("Helvetica", "18"))
    labelAdmin.place(x=10, y= 10)
    
    PanelStatus_admin = PanedWindow(window_admin, width=250, height=100, relief="sunken")
    PanelStatus_admin.place(x=40, y=80)

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
    
    panel_Categoria = PanedWindow(window_admin, height=140, width=250, relief="sunken")
    panel_Categoria.place(x=40, y= 190)

    label_dropdown_admin = Label(panel_Categoria, text ="Catogoria:",font = ("Helvetica", "10"))
    label_dropdown_admin.place(x=10, y= 12)

    Filtrar_dropdown_admin = StringVar()
    txt_dropdown_admin = Entry(panel_Categoria, width=25, textvariable=Filtrar_dropdown_admin)
    txt_dropdown_admin.place(x=75, y= 15)

    btn_Dropdown_adicionar = Button(panel_Categoria, text="Adicionar",font = ("Helvetica", "10"), width=11, height=2, command = lambda: Categoria_Optionsadmin(txt_dropdown_admin.get()))
    btn_Dropdown_adicionar.place(x=20, y=45)

    btn_Dropdown_remover = Button(panel_Categoria, text="Remover",font = ("Helvetica", "10"), width=11, height=2, command = lambda: Categoria_Removeadmin(categoria.get()))
    btn_Dropdown_remover.place(x=130, y=45)

    btnSair_admin = Button(window_admin, text = "Sair", width = 11, height = 4,font = ("Helvetica", "10"), command = lambda: VoltarMenu(window_admin))
    btnSair_admin.place(y=280, x=950)

    
    texto = ReadFiles("Ficheiros\categorias.txt")
    options = str(texto[0]).split(";")
    global dropdown_admin
    categoria = StringVar()
    
    dropdown_admin = ttk.Combobox(panel_Categoria, textvariable= categoria,values= options, state="readonly",width=35)
    dropdown_admin.place(x = 5, y = 100)

def FuncaoSair(window_):
    if userAutenticado.get() != "":
        AdminTreeview_info(userAutenticado.get())
    window_.quit()

def FuncaoSair_noti(WindowPanned, btn):
    WindowPanned.destroy()
    btn.destroy()
    btnNotificacoes.configure(state="active")

def VoltarMenu(window_Tarefas):
    window_Tarefas.destroy()
    window.deiconify()

def updateTreeview(tree,categoria, dataprazo):
    if dataprazo != "":
        #Check dataprazo
                dataprazo = dataprazo.replace("/","-")
                dataprazo = dataprazo.replace(".","-")
                try:
                    dataComp = datetime.strptime(dataprazo, "%d-%m-%Y")
                except:
                    messagebox.showwarning(title="Erro ao inserir a data", message="Não inseriu a data corretamente. Deve inserir o dia(dd) de seguida o mes(mm) e de seguida o ano(yyyy)")
                    return 0

    tree.delete(*tree.get_children())
    shoresBruto = readShores()
    exists = False
    existsUser = False
    for i in range(len(shoresBruto)):
        campos = shoresBruto[i].split(";")
        if campos[2] == userAutenticado.get():
            existsUser = True
            if categoria == "" and dataprazo == "":
                tree.insert("","end", values = (campos[0],campos[6], campos[3], campos[5],campos[4],campos[7]))
                exists = True
            elif categoria == campos[5].strip():
                tree.insert("","end", values = (campos[0],campos[6], campos[3], campos[5],campos[4],campos[7]))
                exists = True
            elif  dataprazo == campos[4].strip():
                tree.insert("","end", values = (campos[0],campos[6], campos[3], campos[5],campos[4],campos[7]))
                exists = True
            elif dataprazo == campos[4].strip() and categoria == campos[5].strip():
                tree.insert("","end", values = (campos[0],campos[6], campos[3], campos[5],campos[4],campos[7]))
                exists = True
    
    if existsUser == False and exists == False:
        messagebox.showwarning(title="User sem tarefas", message="Utilizador não tem tarefas")
    elif exists == False:
        messagebox.showwarning(title="Erro ao filtrar dados", message="Não existem tarefas que estejam dentro dos filtros selecionados")
        
def Open_Tarefas():
    window.withdraw()
    Window_Tarefas = Toplevel() #Insere no topo do ecrã 
    Window_Tarefas.title("Tarefas")
    Window_Tarefas.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    Window_Tarefas.resizable(False,False)
    Window_Tarefas.overrideredirect(True) 

    barraMenu = Menu(Window_Tarefas)
    barraMenu.add_command(label = "Pagina Principal", command= lambda:VoltarMenu(Window_Tarefas))
    barraMenu.add_command(label = "Sair", command= lambda:FuncaoSair(Window_Tarefas))
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
    categorias.append("")

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

    button_Filtrar = Button(lFrame,text="Filtrar", width= 20,height=1, font=("",10), bd=2,  command=lambda : updateTreeview(tree, drop.get(), DataPrazo_Entry.get()))
    button_Filtrar.place(x = 50, y = 180)

    #Botão criar
    button_Criar = Button(Window_Tarefas,text="Criar", width= 28,height=2, font=("",12), bd=2,  command=lambda:criarTarefa(Window_Tarefas, tree, drop.get(), DataPrazo_Entry.get()))
    button_Criar.place(x = 15, y = 380)

    #Botão editar
    button_Editar = Button(Window_Tarefas,text="Editar", width= 28,height=2, font=("",12), bd=2,  command=lambda:editarTarefa(tree))
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

def criarTarefa(window, tree, categoria2,Dataprazo):
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
    btn=Button(window_criacao, width=20, text="CRIAR TAREFA", command= lambda: [insertTarefa(user.get(),categorias.get(),txttitulo.get(), txtmain.get(1.0,END),"Iniciada",txtdatapz.get(),window_criacao, window),updateTreeview(tree, categoria2, Dataprazo)])
    btn.place(x=395, y=245)

def Encontrar_Edit(Selecionado_id):
    shoresBruto = readShores()
    Selecionado_counter = 0
    for linhas in shoresBruto:
        if userAutenticado.get() ==linhas.split(";")[2]:
            Selecionado_counter += 1
            if Selecionado_counter == Selecionado_id:
                return linhas

def DestroyWindow(window_destroy):
    window_destroy.destroy()

def editarTarefa(tree):
    Selecionado = tree.focus()
    if Selecionado == "":
        messagebox.showerror("Edição", "Nenhum item selecionado")
        return
    Selecionado =Selecionado.replace("I","")
    Selecionado = int(Selecionado)
    Linha=Encontrar_Edit(Selecionado)

    
    
    window_atividade_detail = Toplevel()   # Objeto da classe Toplevel, janela principal
    window_atividade_detail.title("Detalhes da Atividade")
    window_atividade_detail.resizable(False,False)
    appWidth_atividade_detail = 550                   
    appHeight_atividade_detail = 300
    screenWidth_atividade_detail = window_atividade_detail.winfo_screenwidth()
    screenHeight_atividade_detail = window_atividade_detail.winfo_screenheight()
    x_atividade_detail = (screenWidth_atividade_detail/2) - (appWidth_atividade_detail/2)
    y_atividade_detail = (screenHeight_atividade_detail/2) - (appHeight_atividade_detail/2)
    window_atividade_detail.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth_atividade_detail, appHeight_atividade_detail, int(x_atividade_detail), int(y_atividade_detail)))
    window_atividade_detail.focus_force()  # força o focus na window atual

    # Label Titulo
    labelTitulo_atividade_detail = Label(window_atividade_detail, text ="Titulo: ",font = ("Helvetica", "10"))
    labelTitulo_atividade_detail.place(x=15, y= 62)
    txtTitulo_atividade_detail_VARIAVEL = StringVar()
    txtTitulo_atividade_detail_VARIAVEL.set(Linha.split(";")[6])
    txtTitulo_atividade_detail = Entry(window_atividade_detail, width=25, textvariable=txtTitulo_atividade_detail_VARIAVEL, state="disable")
    txtTitulo_atividade_detail.place(x=55, y= 65)
    # Label DataLimite
    labeldataLimite_atividade_detail = Label(window_atividade_detail, text ="Data Prazo: ",font = ("Helvetica", "10"))
    labeldataLimite_atividade_detail.place(x=15, y= 197)
    DataLimite = StringVar()
    DataLimite.set(Linha.split(";")[4])
    txtdataLimite_atividade_detail = Entry(window_atividade_detail, width=25, textvariable=DataLimite, state="disable")
    txtdataLimite_atividade_detail.place(x=100, y= 200)
    #Comentario
    labelComentario_atividade_detail = Label(window_atividade_detail, text ="Comentarios: ",font = ("Helvetica", "10"))
    labelComentario_atividade_detail.place(x=15, y= 102)
    txtComentario_atividade_detail = Text(window_atividade_detail, width=54,height=5)
    txtComentario_atividade_detail.place(x=100, y= 105)
    txtComentario_atividade_detail.insert("end",Linha.split(";")[7])
    txtComentario_atividade_detail.configure(state="disable")

    labeldrop = Label(window_atividade_detail, text ="Categoria:",font = ("Helvetica", "10"))
    labeldrop.place(x=310, y= 58)

    Categoria = StringVar()
    Categoria.set(Linha.split(";")[5])
    txtCat_atividade_detail = Entry(window_atividade_detail, width=25, textvariable=Categoria, state="disable")
    txtCat_atividade_detail.place(x=380, y= 60)

    labelText_Atividade_detail = Label(window_atividade_detail, text ="Detalhe da Atividade",font = ("Helvetica", "30"))
    labelText_Atividade_detail.place(x=100 , y= 5)
    
    btnSair_atividade = Button(window_atividade_detail,image = imagemClose, width = 48, height = 48, command= lambda:DestroyWindow(window_atividade_detail))
    btnSair_atividade.place(x=475, y=235)

    btnEditar_Atividade = Button (window_atividade_detail,image = imgEditar, width = 48, height = 48, command= lambda:Editar_tarefa(Linha, window_atividade_detail))
    btnEditar_Atividade.place(x=407 , y=235)

    btnEleminar = Button(window_atividade_detail,image = imgEleminar, width = 48, height = 48, command= lambda:eliminateTarefa(Linha.split(";")[2],Linha.split(";")[6],Linha.split(";")[4],window_atividade_detail))
    btnEleminar.place(x=339 , y=235)

def Editar_tarefa(Linha, window_Atividade):
    window_Atividade.destroy()
    window_atividade_Editar = Toplevel()   # Objeto da classe Toplevel, janela principal
    window_atividade_Editar.title("Editar Atividade")
    window_atividade_Editar.resizable(False,False)
    appWidth_atividade_detail = 550                   
    appHeight_atividade_detail = 300
    screenWidth_atividade_detail = window_atividade_Editar.winfo_screenwidth()
    screenHeight_atividade_detail = window_atividade_Editar.winfo_screenheight()
    x_atividade_detail = (screenWidth_atividade_detail/2) - (appWidth_atividade_detail/2)
    y_atividade_detail = (screenHeight_atividade_detail/2) - (appHeight_atividade_detail/2)
    window_atividade_Editar.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth_atividade_detail, appHeight_atividade_detail, int(x_atividade_detail), int(y_atividade_detail)))
    window_atividade_Editar.focus_force()  # força o focus na window atual

        # Label Titulo
    labelTitulo_atividade_detail = Label(window_atividade_Editar, text ="Titulo: ",font = ("Helvetica", "10"))
    labelTitulo_atividade_detail.place(x=15, y= 62)
    txtTitulo_atividade_detail_VARIAVEL = StringVar()
    txtTitulo_atividade_detail_VARIAVEL.set(Linha.split(";")[6])
    txtTitulo_atividade_detail = Entry(window_atividade_Editar, width=25, textvariable=txtTitulo_atividade_detail_VARIAVEL)
    txtTitulo_atividade_detail.place(x=55, y= 65)
    # Label DataLimite
    labeldataLimite_atividade_detail = Label(window_atividade_Editar, text ="Data Prazo: ",font = ("Helvetica", "10"))
    labeldataLimite_atividade_detail.place(x=15, y= 197)
    DataLimite = StringVar()
    DataLimite.set(Linha.split(";")[4])
    txtdataLimite_atividade_detail = Entry(window_atividade_Editar, width=25, textvariable=DataLimite)
    txtdataLimite_atividade_detail.place(x=100, y= 200)
    #Comentario
    labelComentario_atividade_detail = Label(window_atividade_Editar, text ="Comentarios: ",font = ("Helvetica", "10"))
    labelComentario_atividade_detail.place(x=15, y= 102)
    txtComentario_atividade_detail = Text(window_atividade_Editar, width=54,height=5)
    txtComentario_atividade_detail.place(x=100, y= 105)
    txtComentario_atividade_detail.insert("end",Linha.split(";")[7])

    labeldrop = Label(window_atividade_Editar, text ="Categoria:",font = ("Helvetica", "10"))
    labeldrop.place(x=310, y= 58)

    texto = ReadFiles("Ficheiros\categorias.txt")
    categorias = str(texto[0]).split(";")
    categoria = StringVar()
    
    drop = ttk.Combobox(window_atividade_Editar, values=categorias, state="readonly",textvariable=categoria)
    drop.place(x=380, y= 60)

    labelText_Atividade_detail = Label(window_atividade_Editar, text ="Editar Atividade",font = ("Helvetica", "30"))
    labelText_Atividade_detail.place(x=140 , y= 5)

    Estados = LabelFrame(window_atividade_Editar, width=250, height=50, relief="sunken", text="Estado")
    Estados.place(x= 15, y=220)

    Radio_value = StringVar()
    Radio_value.set(Linha.split(";")[3])
    rd1= Radiobutton(Estados, text= "Iniciada", value= "Iniciada", variable=Radio_value)
    rd2= Radiobutton(Estados, text= "Progresso", value= "Progresso", variable=Radio_value)
    rd3= Radiobutton(Estados, text= "Finalizado", value= "Finalizado", variable=Radio_value)
    rd1.place(x=10 , y=5)
    rd2.place(x=80, y=5)
    rd3.place(x=160, y=5)

    btnConfirmar = Button (window_atividade_Editar,image = imgConfirmar, width = 48, height = 48, command=lambda:Editar_Atividade(Linha, txtTitulo_atividade_detail_VARIAVEL.get(),Radio_value.get(),categoria.get(),txtComentario_atividade_detail.get(1.0,"end"), DataLimite.get(),window_atividade_Editar))
    btnConfirmar.place(x=407 , y=235)

    btnDiscard = Button(window_atividade_Editar,image = imgDiscard, width = 48, height = 48, command= lambda:DestroyWindow(window_atividade_Editar))
    btnDiscard.place(x=475 , y=235)

def Noti_criar(username):
    panel_Noti = PanedWindow(ctnCanvas, width=150, height=300, relief="sunken")
    panel_Noti.place(x=30, y=117)

    btnNotificacoes.configure(state="disable")

    btnSair = Button(ctnCanvas, image= imagemCloseNoti, width = 48, height = 48, command= lambda: FuncaoSair_noti(panel_Noti, btnSair))
    btnSair.place(x=127, y=420)

    Texto_Shores = readShores()
    today = date.today()
    today = today.strftime("%d-%m-%Y")
    counter_4 = 0
    for linhas in Texto_Shores:
        if username == linhas.split(";")[2]:
            counter_4 += 1
            if today > linhas.split(";")[4]:
                if counter_4 == 1:
                    Paned_window1 =PanedWindow(panel_Noti, width=150, height=75,relief="sunken", bg="red")
                    Paned_window1.place(x=0,y=0 )

                    Label_1=StringVar()
                    Adder = "Titulo:  " + linhas.split(";")[6]
                    Label_1.set(Adder)
                    lbl_paned_1 = Label(Paned_window1, textvariable=Label_1, font=("Helvetica", "8"))
                    lbl_paned_1.place(x= 5, y=5)

                    Label_Cat_1=StringVar()
                    Adder = "Categoria:  " + linhas.split(";")[5]
                    Label_Cat_1.set(Adder)
                    lbl_panedCat_1 = Label(Paned_window1, textvariable=Label_Cat_1, font=("Helvetica", "8"))
                    lbl_panedCat_1.place(x= 5, y=25)

                    Label_Data_1=StringVar()
                    Adder = "Data Limite:  " + linhas.split(";")[4]
                    Label_Data_1.set(Adder)
                    lbl_panedData_1 = Label(Paned_window1, textvariable=Label_Data_1, font=("Helvetica", "8"))
                    lbl_panedData_1.place(x= 5, y=45)
                if counter_4 == 2:
                    Paned_window2 =PanedWindow(panel_Noti, width=150, height=75,relief="sunken", bg="red")
                    Paned_window2.place(x=0,y=75)

                    Label_2=StringVar()
                    Adder = "Titulo:  " + linhas.split(";")[6]
                    Label_2.set(Adder)
                    lbl_paned_2 = Label(Paned_window2, textvariable=Label_2, font=("Helvetica", "8"))
                    lbl_paned_2.place(x= 5, y=5)

                    Label_Cat_2=StringVar()
                    Adder = "Categoria:  " + linhas.split(";")[5]
                    Label_Cat_2.set(Adder)
                    lbl_panedCat_2 = Label(Paned_window2, textvariable=Label_Cat_2, font=("Helvetica", "8"))
                    lbl_panedCat_2.place(x= 5, y=25)

                    Label_Data_2=StringVar()
                    Adder = "Data Limite:  " + linhas.split(";")[4]
                    Label_Data_2.set(Adder)
                    lbl_panedData_2 = Label(Paned_window2, textvariable=Label_Data_2, font=("Helvetica", "8"))
                    lbl_panedData_2.place(x= 5, y=45)
                if counter_4 == 3:
                    Paned_window3 =PanedWindow(panel_Noti, width=150, height=75,relief="sunken", bg="red")
                    Paned_window3.place(x=0,y=150 )

                    Label_3=StringVar()
                    Adder = "Titulo:  " + linhas.split(";")[6]
                    Label_3.set(Adder)
                    lbl_paned_3 = Label(Paned_window3, textvariable=Label_3, font=("Helvetica", "8"))
                    lbl_paned_3.place(x= 5, y=5)

                    Label_Cat_3=StringVar()
                    Adder = "Categoria:  " + linhas.split(";")[5]
                    Label_Cat_3.set(Adder)
                    lbl_panedCat_3 = Label(Paned_window3, textvariable=Label_Cat_3, font=("Helvetica", "8"))
                    lbl_panedCat_3.place(x= 5, y=25)

                    Label_Data_3=StringVar()
                    Adder = "Data Limite:  " + linhas.split(";")[4]
                    Label_Data_3.set(Adder)
                    lbl_panedData_3 = Label(Paned_window3, textvariable=Label_Data_3, font=("Helvetica", "8"))
                    lbl_panedData_3.place(x= 5, y=45)
                if counter_4 == 4:
                    Paned_window4 =PanedWindow(panel_Noti, width=150, height=75,relief="sunken", bg="red")
                    Paned_window4.place(x=0,y=225)

                    Label_4=StringVar()
                    Adder = "Titulo:  " + linhas.split(";")[6]
                    Label_4.set(Adder)
                    lbl_paned_4 = Label(Paned_window4, textvariable=Label_4, font=("Helvetica", "8"))
                    lbl_paned_4.place(x= 5, y=5)

                    Label_Cat_4=StringVar()
                    Adder = "Categoria:  " + linhas.split(";")[5]
                    Label_Cat_4.set(Adder)
                    lbl_panedCat_4 = Label(Paned_window4, textvariable=Label_Cat_4, font=("Helvetica", "8"))
                    lbl_panedCat_4.place(x= 5, y=25)

                    Label_Data_4=StringVar()
                    Adder = "Data Limite:  " + linhas.split(";")[4]
                    Label_Data_4.set(Adder)
                    lbl_panedData_4 = Label(Paned_window4, textvariable=Label_Data_4, font=("Helvetica", "8"))
                    lbl_panedData_4.place(x= 5, y=45)
            if today == linhas.split(";")[4]:
                if counter_4 == 1:
                    Paned_window1 =PanedWindow(panel_Noti, width=150, height=75,relief="sunken", bg="yellow")
                    Paned_window1.place(x=0,y=0 )

                    Label_1=StringVar()
                    Adder = "Titulo:  " + linhas.split(";")[6]
                    Label_1.set(Adder)
                    lbl_paned_1 = Label(Paned_window1, textvariable=Label_1, font=("Helvetica", "8"))
                    lbl_paned_1.place(x= 5, y=5)

                    Label_Cat_1=StringVar()
                    Adder = "Categoria:  " + linhas.split(";")[5]
                    Label_Cat_1.set(Adder)
                    lbl_panedCat_1 = Label(Paned_window1, textvariable=Label_Cat_1, font=("Helvetica", "8"))
                    lbl_panedCat_1.place(x= 5, y=25)

                    Label_Data_1=StringVar()
                    Adder = "Data Limite:  " + linhas.split(";")[4]
                    Label_Data_1.set(Adder)
                    lbl_panedData_1 = Label(Paned_window1, textvariable=Label_Data_1, font=("Helvetica", "8"))
                    lbl_panedData_1.place(x= 5, y=45)
                if counter_4 == 2:
                    Paned_window2 =PanedWindow(panel_Noti, width=150, height=75,relief="sunken", bg="yellow")
                    Paned_window2.place(x=0,y=75 )

                    Label_2=StringVar()
                    Adder = "Titulo:  " + linhas.split(";")[6]
                    Label_2.set(Adder)
                    lbl_paned_2 = Label(Paned_window2, textvariable=Label_2, font=("Helvetica", "8"))
                    lbl_paned_2.place(x= 5, y=5)

                    Label_Cat_2=StringVar()
                    Adder = "Categoria:  " + linhas.split(";")[5]
                    Label_Cat_2.set(Adder)
                    lbl_panedCat_2 = Label(Paned_window2, textvariable=Label_Cat_2, font=("Helvetica", "8"))
                    lbl_panedCat_2.place(x= 5, y=25)

                    Label_Data_2=StringVar()
                    Adder = "Data Limite:  " + linhas.split(";")[4]
                    Label_Data_2.set(Adder)
                    lbl_panedData_2 = Label(Paned_window2, textvariable=Label_Data_2, font=("Helvetica", "8"))
                    lbl_panedData_2.place(x= 5, y=45)
                if counter_4 == 3:
                    Paned_window3 =PanedWindow(panel_Noti, width=150, height=75,relief="sunken", bg="yellow")
                    Paned_window3.place(x=0,y=150 )

                    Label_3=StringVar()
                    Adder = "Titulo:  " + linhas.split(";")[6]
                    Label_3.set(Adder)
                    lbl_paned_3 = Label(Paned_window3, textvariable=Label_3, font=("Helvetica", "8"))
                    lbl_paned_3.place(x= 5, y=5)

                    Label_Cat_3=StringVar()
                    Adder = "Categoria:  " + linhas.split(";")[5]
                    Label_Cat_3.set(Adder)
                    lbl_panedCat_3 = Label(Paned_window3, textvariable=Label_Cat_3, font=("Helvetica", "8"))
                    lbl_panedCat_3.place(x= 5, y=25)

                    Label_Data_3=StringVar()
                    Adder = "Data Limite:  " + linhas.split(";")[4]
                    Label_Data_3.set(Adder)
                    lbl_panedData_3 = Label(Paned_window3, textvariable=Label_Data_3, font=("Helvetica", "8"))
                    lbl_panedData_3.place(x= 5, y=45)
                if counter_4 == 4:
                    Paned_window4 =PanedWindow(panel_Noti, width=150, height=75,relief="sunken", bg="yellow")
                    Paned_window4.place(x=0,y=225 )

                    Label_4=StringVar()
                    Adder = "Titulo:  " + linhas.split(";")[6]
                    Label_4.set(Adder)
                    lbl_paned_4 = Label(Paned_window4, textvariable=Label_4, font=("Helvetica", "8"))
                    lbl_paned_4.place(x= 5, y=5)

                    Label_Cat_4=StringVar()
                    Adder = "Categoria:  " + linhas.split(";")[5]
                    Label_Cat_4.set(Adder)
                    lbl_panedCat_4 = Label(Paned_window4, textvariable=Label_Cat_4, font=("Helvetica", "8"))
                    lbl_panedCat_4.place(x= 5, y=25)

                    Label_Data_4=StringVar()
                    Adder = "Data Limite:  " + linhas.split(";")[4]
                    Label_Data_4.set(Adder)
                    lbl_panedData_4 = Label(Paned_window4, textvariable=Label_Data_4, font=("Helvetica", "8"))
                    lbl_panedData_4.place(x= 5, y=45)

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

imagemNoti = PhotoImage(file="imagens\\NotiIcon.png")
imagemCloseNoti = PhotoImage(file="imagens\\xIcon.png")
imagemClose = PhotoImage(file="imagens\\xIconClose.png")
imgFinalizar = PhotoImage(file="imagens\\CheckmarkIcon.png")
imgEditar = PhotoImage(file="imagens\\EditarIcon.png")
imgEleminar = PhotoImage(file="imagens\\EleminarIcon.png")
imgDiscard = PhotoImage(file="imagens\\xIconClose.png")
imgConfirmar = PhotoImage(file="imagens\\CheckmarkIcon.png")

global img
img = PhotoImage(file = ".\imagens\\Background.png")
ctnCanvas.create_image(550, 300, image = img)

window.mainloop()
