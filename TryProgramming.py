print('''
Para crear una pagina web se usa HTML\n
En el block de notas de abajo necesito\n
que le digas a la maquina que vas a \n
crear una pagina web.\n
eso se hace escribiendo <html>\n
Pero tambien dile que tendra un final\n
y eso se hace con </html>\n
Por lo que te quedara algo asi.\n
<html>\n
</html>
''')
Abrir_pagina="a"
Cierra_pagina="a"
while(Abrir_pagina!="<html>"):
    Abrir_pagina=input("Abre la pagina >> ")
while(Cierra_pagina!="</html>"):
    Cierra_pagina=input("Cierra la pagina >> ")
