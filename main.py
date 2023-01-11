import Handle_Shores
from tkinter import *
from tkinter import ttk

user="user"
categoria = "Desporto"
titulo ="Sub21"
estado = "criada"
conteudo = "Tem que haver mais bolas"
data_hora = "25-12-2022 17:00:40"
campo = "titulo"
data_prazo = "05-10-2022"

options = ["Nenhuma", "Desporto"]

def Open_Tarefas():
    window.withdraw()
    Window_Tarefas = Toplevel() #Insere no topo do ecrã 
    Window_Tarefas.title("Tarefas")
    Window_Tarefas.geometry(f'{appwidth}x{appHeight}+{int(x)}+{int(y)}')
    Window_Tarefas.focus_force()
    Window_Tarefas.grab_set()

    barraMenu = Menu(Window_Tarefas)
    barraMenu.add_command(label = "Pagina Principal", command= "")
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
    drop = ttk.Combobox(lFrame, textvariable= categoria, values= options, state="readonly", font=("",10))
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
    button_Criar = Button(Window_Tarefas,text="Criar", width= 28,height=2, font=("",12), bd=2,  command="")
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




    



window = Tk()
appwidth = 1100
appHeight = 600
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
x = (screenWidth/2) - (appwidth/2)
y= (screenHeight/2) - (appHeight/2)
window.geometry(f'{appwidth}x{appHeight}+{int(x)}+{int(y)}')

window.title("")


Open_Tarefas()

window.mainloop()