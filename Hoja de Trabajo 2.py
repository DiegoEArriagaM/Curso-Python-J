print("________________Ejercicio 1________________")
#Peticion del número
x=int(input("Ingrese un número entero: "))

for i in range(1,x+1):
    for j in range(1,i+1):
        print('*',end="")
    print("")   

print("________________Ejercicio 2________________") 
x=int(input("Ingrese un número entero distinto de 0 o 1: "))

y=True
for i in range(1,x+1):
    if x%i==0 and i!=x and i!=1:
        print(x,"No es primo")
        y=False
        break
if y==True:
    print(x,"Es primo")