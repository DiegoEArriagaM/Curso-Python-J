'''
Comentario
Multi
Linea
'''
#Python usa sangría para indicar un bloque de código.
if 5>2:
    print('Cinco es mayor que Dos')

#El numero de espacios depende del programador, pero debe ser al menos una
if 5>2:
                        print('Hola mundo')

#Tiene que usar la misma cantidad espacios en el mismo bloque de código,
# de lo contrario Python dará error.
if 5>2:
    print('Cinco es mayor que Dos')
    print('Hola mundo')
    if 4>1:
        print('Cuatro es mayor que Uno')

#Python no tiene ningún comando para declarar una variable
#Las variables de cadena se pueden declarar utilizando comillas simples o dobles
mivariable=0
x=5.10
y="Hola mundo"
x1=5
y2="Jessica"
print(x1)
print(y2)

#Las variables pueden cambiar de tipo una vez se hayan establecido
x=4
x='Sandy'
print(x)

x,y,z="Orange","Banana","Cherry"
print(x)
print(y)
print(z)

x=y=z="Orange"
print(x)
print(y)
print(z)

x="Aweson"
y="Otro texto"
print("Python es "+x+"    "+y)

x=5
y=10
print(x+y)

#Si se intenta combinar texto y numeros de hacerlo de la siguiente manera:
x=5
y="Años"
z=10
print(x,z,y)

#Metodo
def mifuncion():
    print(y2)

mifuncion()