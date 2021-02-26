"""
*********IMPORTANT************

INSTALL ON CMD(python3):

pip install pillow
pip install mysql-connector
pip install mysql-connector-python
pip install mysql-connector-python-rf


# mostrar a tabela:
c.execute("SELECT * FROM clientes")
print(c.description)

for item in c.description:
    print(item)


"""

from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

pcolor = '#e5eaff'
scolor = 'black'
tcolor = '#d1d6ff'

root = Tk()
root.title('Registro')
root.geometry("400x600")
root['bg'] = pcolor

Register_frame = Frame(root, bg=(pcolor), height=200, width=510)
Register_frame.place(x=0, y=0)

# Databases

# Criar ou conectar a um bando de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Senh410@",
    database="meu_estacionamento"

)


# criar um cursor e inicia-lo
c = mydb.cursor()

# Usar a linha abaixo para criar o banco de dados pela primeira vez
c.execute("CREATE DATABASE IF NOT EXISTS meu_estacionamento")


c.execute("SHOW DATABASES")
for db in c:
    print(db)

# Excluir tabela:
#c.execute("DROP TABLE clientes")


# Criar tabela no banco de dados
# Usar a linha abaixo para criar a tabela pela primeira vez

c.execute("CREATE TABLE IF NOT EXISTS clientes (user_id INT AUTO_INCREMENT PRIMARY KEY,\
    nome VARCHAR(255) ,\
    email VARCHAR(255),\
    cep INT(10),\
    cidade VARCHAR(255),\
    estado VARCHAR(255),\
    pais VARCHAR(255),\
    metodo_pagamento VARCHAR(255),\
    desconto VARCHAR(255),\
    sobrenome VARCHAR(255),\
    endereco VARCHAR(255), \
    placa_carro VARCHAR(10),\
    preco DECIMAL(10,2))")


def modoClarofun():

    global pcolor, scolor, tcolor

    pcolor = '#e5eaff'
    scolor = 'black'
    tcolor = '#d1d6ff'

    root.config(background=pcolor)
    Register_frame.config(bg=pcolor)

    titulolbl.config(background=pcolor, fg=scolor)

    modoClarobtn.config(bg=tcolor, fg=scolor)
    modoClarobtn["state"] = "disabled"

    modoEscurobtn.config(bg='#585463', fg=scolor)
    modoEscurobtn["state"] = "normal"
    nomelbl.config(bg=pcolor, fg=scolor)
    sobrenomelbl.config(bg=pcolor, fg=scolor)
    enderecolbl.config(bg=pcolor, fg=scolor)
    placa_carrolbl.config(bg=pcolor, fg=scolor)
    precolbl.config(bg=pcolor, fg=scolor)
    emaillbl.config(bg=pcolor, fg=scolor)
    ceplbl.config(bg=pcolor, fg=scolor)
    cidadelbl.config(bg=pcolor, fg=scolor)
    estadolbl.config(bg=pcolor, fg=scolor)
    paislbl.config(bg=pcolor, fg=scolor)
    metodo_pagamentolbl.config(bg=pcolor, fg=scolor)
    descontolbl.config(bg=pcolor, fg=scolor)

    add_clientebtn.config(bg=tcolor, fg=scolor)
    limpar_clientebtn.config(bg=tcolor, fg=scolor)


def modoEscurofun():

    global pcolor, scolor, tcolor

    pcolor = 'black'
    scolor = '#696969'
    tcolor = '#585463'

    root.config(background=pcolor)
    Register_frame.config(bg=pcolor)

    titulolbl.config(background=pcolor, fg=scolor)

    modoClarobtn.config(bg='#e5eaff', fg='black')
    modoClarobtn["state"] = "normal"

    modoEscurobtn.config(bg=tcolor, fg='black')
    modoEscurobtn["state"] = "disabled"
    nomelbl.config(bg=pcolor, fg=scolor)
    sobrenomelbl.config(bg=pcolor, fg=scolor)
    enderecolbl.config(bg=pcolor, fg=scolor)
    placa_carrolbl.config(bg=pcolor, fg=scolor)
    precolbl.config(bg=pcolor, fg=scolor)
    emaillbl.config(bg=pcolor, fg=scolor)
    ceplbl.config(bg=pcolor, fg=scolor)
    cidadelbl.config(bg=pcolor, fg=scolor)
    estadolbl.config(bg=pcolor, fg=scolor)
    paislbl.config(bg=pcolor, fg=scolor)
    metodo_pagamentolbl.config(bg=pcolor, fg=scolor)
    descontolbl.config(bg=pcolor, fg=scolor)

    add_clientebtn.config(bg=tcolor, fg='black')
    limpar_clientebtn.config(bg=tcolor, fg='black')


def limpar_campos():
    nomebox.delete(0, END)
    sobrenomebox.delete(0, END)
    enderecobox.delete(0, END)
    placa_carrobox.delete(0, END)
    precobox.delete(0, END)
    emailbox.delete(0, END)
    cepbox.delete(0, END)
    cidadebox.delete(0, END)
    estadobox.delete(0, END)
    paisbox.delete(0, END)
    metodo_pagamentobox.delete(0, END)
    descontobox.delete(0, END)


titulolbl = Label(root, text="Meu estacionamento", font=(
    "Helvetica", 14), background=pcolor, fg=scolor)
titulolbl.place(x=-10, y=0, relwidth=1)

modoClarobtn = Button(Register_frame, text="Modo claro ",
                      fg=scolor, bg=tcolor, command=modoClarofun)
modoClarobtn["state"] = "disabled"
modoClarobtn.grid(row=1, column=0, columnspan="2", pady=35)

modoEscurobtn = Button(Register_frame, text="Modo Escuro",
                       fg='white', bg='#585463', command=modoEscurofun)
modoEscurobtn.grid(row=1, column=1, columnspan="2", sticky=E)

nomelbl = Label(Register_frame, text="Nome:", bg=pcolor, fg=scolor)
nomelbl.grid(row=2, column=0, pady=1, stick=W, padx=10)

sobrenomelbl = Label(Register_frame, text="Sobrenome:", bg=pcolor, fg=scolor)
sobrenomelbl.grid(row=3, column=0, pady=1, stick=W, padx=10)

enderecolbl = Label(Register_frame, text="Endereco:", bg=pcolor, fg=scolor)
enderecolbl.grid(row=4, column=0, pady=1, stick=W, padx=10)

placa_carrolbl = Label(
    Register_frame, text="Placa carro:", bg=pcolor, fg=scolor)
placa_carrolbl.grid(row=5, column=0, pady=1, stick=W, padx=10)

precolbl = Label(Register_frame, text="Preço:", bg=pcolor, fg=scolor)
precolbl.grid(row=6, column=0, pady=1, stick=W, padx=10)

emaillbl = Label(Register_frame, text="E-mail:", bg=pcolor, fg=scolor)
emaillbl.grid(row=7, column=0, pady=1, stick=W, padx=10)

ceplbl = Label(Register_frame, text="CEP:", bg=pcolor, fg=scolor)
ceplbl.grid(row=8, column=0, pady=1, stick=W, padx=10)

cidadelbl = Label(Register_frame, text="Cidade:", bg=pcolor, fg=scolor)
cidadelbl.grid(row=9, column=0, pady=1, stick=W, padx=10)

estadolbl = Label(Register_frame, text="Estado:", bg=pcolor, fg=scolor)
estadolbl.grid(row=10, column=0, pady=1, stick=W, padx=10)

paislbl = Label(Register_frame, text="País:", bg=pcolor, fg=scolor)
paislbl.grid(row=11, column=0, pady=1, stick=W, padx=10)

metodo_pagamentolbl = Label(
    Register_frame, text="Metodo pagamento:", bg=pcolor, fg=scolor)
metodo_pagamentolbl.grid(row=12, column=0, pady=1, stick=W, padx=10)

descontolbl = Label(Register_frame, text="Desconto:", bg=pcolor, fg=scolor)
descontolbl.grid(row=13, column=0, pady=1, stick=W, padx=10)

# Entrada de dados:
nomebox = Entry(Register_frame)
nomebox.grid(row=2, column=1)

sobrenomebox = Entry(Register_frame)
sobrenomebox.grid(row=3, column=1, padx=5)

enderecobox = Entry(Register_frame)
enderecobox.grid(row=4, column=1, padx=5)

placa_carrobox = Entry(Register_frame)
placa_carrobox.grid(row=5, column=1, padx=5)

precobox = Entry(Register_frame)
precobox.grid(row=6, column=1, padx=5)

emailbox = Entry(Register_frame)
emailbox.grid(row=7, column=1, padx=5)

cepbox = Entry(Register_frame)
cepbox.grid(row=8, column=1, padx=5)

cidadebox = Entry(Register_frame)
cidadebox.grid(row=9, column=1, padx=5)

estadobox = Entry(Register_frame)
estadobox.grid(row=10, column=1, padx=5)

paisbox = Entry(Register_frame)
paisbox.grid(row=11, column=1, padx=5)

metodo_pagamentobox = Entry(Register_frame)
metodo_pagamentobox.grid(row=12, column=1, padx=5)

descontobox = Entry(Register_frame)
descontobox.grid(row=13, column=1, padx=5)

clientebox = Entry(Register_frame)
clientebox.grid(row=14, column=1, padx=5)

botelhobox = Entry(Register_frame)
botelhobox.grid(row=15, column=1, padx=5)

# Add funcionario
add_clientebtn = Button(
    Register_frame, text="Cadastrar o cliente", fg=scolor, bg=tcolor)
add_clientebtn.grid(row=14, column=0, pady=25, padx=10)
limpar_clientebtn = Button(
    Register_frame, text="Limpar seleções", fg=scolor, bg=tcolor, command=limpar_campos)
limpar_clientebtn.grid(row=14, column=1, pady=10, padx=10)


root.mainloop()
