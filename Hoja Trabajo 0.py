print("Calculo del Indice de masa corporal (IMC)")
#Peticion del peso y la altura
peso=float(input("Por favor ingrese su peso en Kilogramos: "))
altura=float(input("Por favor ingrese su altura en metros: "))

#Calcular IMC
imc=peso/(altura**2)

#Mostrar el resultaro
print("Tu índice de masa corporal es ",round(imc,2))