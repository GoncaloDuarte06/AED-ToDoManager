from tkinter import *
from tkinter import messagebox
import os
from Login_with_tkinter import *


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
        userAutenticado.set("")
        btnIniciarSessao.config(text = "Iniciar Sessão")
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


window = Tk()
window.resizable(False,False)
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1100                             # tamanho (pixeis) da window a criar 1100 / 700
appHeight = 700 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Gestor de Tarefas')

PanelStatus = PanedWindow(window, width=1100, height=100, relief = "sunken")
PanelStatus.place(x=0, y=0)

btnVerAtividades = Button(PanelStatus, text = "Ver Atividades", width = 11, height = 4,font = ("Helvetica", "10"))
btnVerAtividades.place(x=50, y=12)
btnCriarAtividade = Button(PanelStatus, text = "Criar Atividades", width = 11, height = 4,font = ("Helvetica", "10"))
btnCriarAtividade.place(x=160, y=12)

global btnIniciarSessao
imageLogin = PhotoImage(file = "imagens\\icoLogin.png")
btnIniciarSessao = Button (PanelStatus, image = imageLogin, text = "Iniciar Sessão", width = 95, height = 68, compound=TOP,font = ("Helvetica", "10"), command=Login_tk)
btnIniciarSessao.place(x=850, y=12)

imageConta = PhotoImage(file = "imagens\\icoConta.png" )
btnCriarConta = Button (PanelStatus, image = imageConta,  text = "Criar Conta", width = 95, height = 68, compound=TOP,font = ("Helvetica", "10"), command=Criar_conta_TK)
btnCriarConta.place(x=960, y=12)


global userAutenticado
userAutenticado = StringVar()
userAutenticado.set("")
labelHeader = Label(PanelStatus, textvariable= userAutenticado, fg = "red", font=("Helvetica", "20"))
labelHeader.place(x= 280, y= 32)



panel2 = PanedWindow(window, width=1100, height=600)
panel2.place(x=0, y=98)
ctnCanvas = Canvas(panel2, width = 1100, height= 600)
ctnCanvas.place(x=0, y= 0)
global img
img = PhotoImage(file = ".\imagens\\1100x600.png")
ctnCanvas.create_image(550, 300, image = img)





window.mainloop()
