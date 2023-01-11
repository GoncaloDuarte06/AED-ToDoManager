
from tkinter import *
from tkinter.ttk import Combobox


class application:
    def __init__(self, master=None):
     pass

import os
window = Tk()
application(window)
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 550                             # tamanho (pixeis) da window a criar 900 / 500
appHeight = 300
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Criação de tarefa')


#Label 
lbltitulo= Label(window, text = "TITULO", font=("helvetica", 8))
lbltitulo.place(x=7, y=60)

lbldatapz= Label(window,text= "DATA PRAZO", font=("helvetica", 8))
lbldatapz.place(x=7,y=275)

lbluser= Label(window,text= "USER", font=("helvetica", 8))
lbluser.place(x=505, y=10)

lblcomentario= Label(window,text= "COMENTARIO", font=("helvetica", 8))
lblcomentario.place(x=7, y=110)

lblcategorias= Label(window,text= "CATEGORIAS", font=("helvetica", 8))
lblcategorias.place(x=8, y=10)

#Box
txtcategorias = Entry(window, width=20)
txtcategorias.place(x=10, y=30)

txtconteudo = Entry(window, width=88)
txtconteudo.place(x=10, y=80)

txtmain = Text(window, width=66, height = 6)
txtmain.place(x=10, y=130)

txtdatapz = Entry(window, width=20)
txtdatapz.place(x=10, y=250)

#Button
btn=Button(window, width=20, text="CRIAR TAREFA")
btn.place(x=395, y=245)

#dropdownlist
lista = []
user = Combobox(window, values=lista)
user.place (x=399, y=30)


window.mainloop()
