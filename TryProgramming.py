import tkinter as tk
from tkinter import *
from tkinter import ttk

def salir(event=None):
	Ventana.destroy()

Ventana=tk.Tk()
Ventana.attributes("-fullscreen", True)
Ventana.title("Try Programming")
Ventana.resizable(0,0)
Ventana.bind_all("<Control-z>", salir)
label1=tk.Label(text="El Formato de una web debe ser el siguiente:")
label2=tk.Label(text="<html>")
label3=tk.Label(text="<head>")
label4=tk.Label(text="</head>")
label5=tk.Label(text="<body>")
label6=tk.Label(text="</body>")
label7=tk.Label(text="</html>")
label8=tk.Label(text="La etiqueta <html> y </html> son para que el navegador sepa donde empieza y donde termina la pagina web.")
label9=tk.Label(text="La etiqueta <head> y </head> son para la barra del navegador, luego veremos mas utilidades.")
label10=tk.Label(text="La etiqueta <body> y </body> aqui es donde va toda la informacion de la pagina web y todo lo que se mostrara.")
label1.place(x=10,y=10)
label2.place(x=10,y=40)
label3.place(x=10,y=60)
label4.place(x=10,y=80)
label5.place(x=10,y=100)
label6.place(x=10,y=120)
label7.place(x=10,y=140)
label8.place(x=10,y=180)
label9.place(x=10,y=200)
label10.place(x=10,y=220)

Ventana.txt=tk.Text()
Ventana.txt.insert(1.0,'''"Borra este mensaje y escribe como es la estructura de la web"''')
Ventana.txt.place(x=10,y=250)

Ventana.mainloop()





'''
import os
print(
Para crear una pagina web se usa HTML\n
En el block de notas de abajo necesito\n
que le digas a la maquina que vas a \n
crear una pagina web.\n
eso se hace escribiendo <html>\n
Pero tambien dile que tendra un final\n
y eso se hace con </html>\n
Por lo que te quedara algo asi.\n
<html>\n
</html>)
Abrir_pagina="a"
Cierra_pagina="a"
while(Abrir_pagina!="<html>"):
    Abrir_pagina=input("Abre la pagina >> ")
while(Cierra_pagina!="</html>"):
    Cierra_pagina=input("Cierra la pagina >> ")
os.system("clear")
'''
