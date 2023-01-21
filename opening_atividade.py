from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk


options = []





window_atividade_detail = Tk()   # Objeto da classe Toplevel, janela principal
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
window_atividade_detail.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)

# Label
labelTitulo_atividade_detail = Label(window_atividade_detail, text ="Titulo: ",font = ("Helvetica", "10"))
labelTitulo_atividade_detail.place(x=15, y= 62)
txtTitulo_atividade_detail_VARIAVEL = StringVar()
txtTitulo_atividade_detail = Entry(window_atividade_detail, width=25, textvariable=txtTitulo_atividade_detail_VARIAVEL, state="disable")
txtTitulo_atividade_detail.place(x=55, y= 65)
# Username
labeldataLimite_atividade_detail = Label(window_atividade_detail, text ="Data Prazo: ",font = ("Helvetica", "10"))
labeldataLimite_atividade_detail.place(x=15, y= 197)
userName = StringVar()
txtdataLimite_atividade_detail = Entry(window_atividade_detail, width=25, textvariable=userName, state="disable")
txtdataLimite_atividade_detail.place(x=100, y= 200)
#Password
labelComentario_atividade_detail = Label(window_atividade_detail, text ="Comentarios: ",font = ("Helvetica", "10"))
labelComentario_atividade_detail.place(x=15, y= 102)
Comentario_atividade_detail = StringVar()
txtComentario_atividade_detail = Text(window_atividade_detail, width=54,height=5, state="disable")
txtComentario_atividade_detail.place(x=100, y= 105)

labeldrop = Label(window_atividade_detail, text ="Categorias",font = ("Helvetica", "10"))
labeldrop.place(x=320, y= 62)
categoria = StringVar()
drop = ttk.Combobox(window_atividade_detail, textvariable= categoria, values= options, state="disable")
drop.place(x = 390, y = 65)

labelText_Atividade_detail = Label(window_atividade_detail, text ="Detalhe da Atividade",font = ("Helvetica", "30"))
labelText_Atividade_detail.place(x=100 , y= 5)

imageClose = PhotoImage(file = "imagens\\icons8-xbox-x-50.png" )
btnClose_Atividade_detail = Button(window_atividade_detail,image = imageClose, text = "Fechar", width=95, height=68,font = ("Helvetica", "15"),compound=TOP)
btnClose_Atividade_detail.place(x=430, y= 210) 


txtComentario_atividade_detail.configure(state="disable")






window_atividade_detail.mainloop()