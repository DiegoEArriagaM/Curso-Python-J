class MyClass:
    edad=18

    def ImprimirEdad(edad):
        print(edad)
    
clase1=MyClass()
print("La edad de MyClass es: ",clase1.edad)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myFu(self):
        print('Mi nombre es: '+self.name)

p1=Person("John", 36)
p2=Person("Fernando Jose Paz", 24)

print(p1.name)
print(p1.age)
p1.myFu()
print('-------------------')
print(p2.name)
print(p2.age)

print('------------------------Clase 7------------------------')
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)

x=Person("Person", "Class Person")
x.printname()

class Student(Person):
    pass

y=Student("Student", "Clase Estudiante")
y.printname()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
y=Student("Diego", "Arriaga")
y.printname()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, finame, laname)

        self.graduation=year
        print(self.firstname,self.year)

    def otroMetodo():
        print('Nuevo Metodo')