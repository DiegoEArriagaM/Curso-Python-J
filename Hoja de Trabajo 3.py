
print('-------------------Ejercicio 1----------------------')
contraseña1=input('Ingrese una contraseña: ')
contraseña2=input('Vuelva ingresar la misma contraseña: ')
if contraseña2.lower()==contraseña1.lower():
    print('La segunda contraseña es la misma que la primera ingresada')
else:
    print('La segunda contraseña NO es la misma que la primera ingresada')

print('-------------------Ejercicio 2----------------------')
letras1=['A','B','C','D','E','F','G','H','I','J','K','L','M']
letras2=['N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nombre=input('Ingrese su nombre: ')
sexo=input('Ingrese su sexo [M/F]: ')

inicial=nombre[0:1]

grupoEncontrado=False

if(sexo=='F' or sexo=='f'):
    for letra in letras1:
        if inicial.lower()==letra.lower():
            print(nombre+' pertenece al grupo A')
            grupoEncontrado=True
            break
    if grupoEncontrado==False:
        print(nombre+' pertenece al grupo B')

elif (sexo=='M' or sexo=='m'):
    for letra in letras2:
        if inicial.lower()==letra.lower():
            print(nombre+' pertenece al grupo A')
            grupoEncontrado=True
            break
    if grupoEncontrado==False:
        print(nombre+' pertenece al grupo B')
else:
    print('Ingrese M o F para poder indicarle un grupo')