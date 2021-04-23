'''
print('---------------------Metodo--------------')
def Sumar1():
    resultado=1+22
    print(resultado)
Sumar1()

print('---------------------Función--------------')
def Sumar2():
    resultado=22+3
    return(resultado)
print(Sumar2())
'''

def myFunction():
    print("Hello from a method")
    print("Bye from a method")
myFunction()

def myFunction(fname):
    print(fname+" Arriaga")

myFunction("Diego")

#Argumento Arbitrario
def myFunction(*kids):
    print(kids[3])

myFunction("Diego","Enrique","Arriaga","Meléndez")

def myFunction(child3,child2,child1):
    print(child1)
    print(child2)
    print(child3)

myFunction(child1="Diego", child2="Emily", child3="Jose")

#Palabra clave arbitraria
def myFunction(**kid):
    print(kid["lname"])
myFunction(fname="Jose",lname="Hérnandez")

def myFunction(country="Noruega"):
    print(country)
myFunction("Brazil")
myFunction()
myFunction("Escosia")

fruits=['apple','banana','cherry']
def myFunction(food):
        for x in food:
            print(x)
myFunction(fruits)

#Recursividad
print('-------------Recursividad--------------------')
def cuenta_regresiva(numero):
    numero-=1
    if numero>0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Boom")
    print("Fin de la función ",numero)

cuenta_regresiva(100)

def factorial(numero):
    print("Valor inicial ->",numero)
    if numero>1:
        numero=numero*factorial(numero-1)
    print("Valor final->",numero)
    return numero
myvariable=factorial(5)
print("El factorial es: ",myvariable)