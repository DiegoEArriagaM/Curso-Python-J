print("Condiciones de Python")

a=100
b=200
if b>a:
    print("b es mayor que a")
print("----------------------------------------------")

a=33
b=33
if b>a:
    print("b es mayor que a")
elif a==b:
    print("a y b son iguales")
print("----------------------------------------------")

a=100
b=33
if b>a:
    print("b es mayor que a")
elif a==b:
    print("a y b son iguales")
else:
    print("a es mayor que b")
print("----------------------------------------------")

a=100
b=33
if b>a:
    print("b es mayor que a")
else:
    print("b no es mayor que a")
print("----------------------------------------------")

a=200
b=33
c=500
if a>b and c>a:
    print("c es mayor a b")
print("----------------------------------------------")

a=200
b=33
c=500
if a>b or a>c:
    print("Una de las condiciones es correctas")
print("----------------------------------------------")