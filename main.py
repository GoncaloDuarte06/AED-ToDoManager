from datetime import datetime
import Handle_Shores


user="user"
categoria = "Desporto"
titulo ="Sub21"
estado = "criada"
conteudo = "Tem que haver mais bolas"
data_hora = "25-12-2022 17:00:40"
campo = "titulo"


Handle_Shores.insert(user,categoria,titulo,conteudo,estado)

Handle_Shores.eliminate(user,titulo,data_hora)

Handle_Shores.edit(user,titulo,data_hora,campo)