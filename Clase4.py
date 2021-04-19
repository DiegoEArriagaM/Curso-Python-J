print("----------------------------Ciclo FOR---------------------------------")
fruits=["apple","banana","cherry","watermelon","berry","peach","lemon"]
for fruit in fruits:
    print(fruit)

print("---------------------------------------------------")
for x in "banana":
    print(x)

print("---------------------------------------------------")
fruits=["apple","cherry","banana","watermelon","berry","peach","lemon"]
for fruit in fruits:
    print(fruit)
    if fruit=="banana":
        break

print("---------------------------------------------------")
fruits=["apple","cherry","banana","watermelon","berry","peach","lemon"]
for fruit in fruits:
    if fruit=="banana":
        break
    print(fruit)

print("---------------------------------------------------")
fruits=["apple","cherry","banana","watermelon","berry","peach","lemon"]
for fruit in fruits:
    if fruit=="banana":
        continue
    print(fruit)

print("---------------------------------------------------")
for x in range(6):
    print(x)

print("---------------------------------------------------")
for x in range(2,6):
    print(x)

print("---------------------------------------------------")
for x in range(2,30,3):
    print(x)

print("---------------------------------------------------")
for x in range(2,6):
    print(x)
else:
    print("Termino el for")

print("---------------------------------------------------")
fruits=["apple","cherry","banana","watermelon","berry","peach","lemon"]
adj=["red","big","tasty"]

for x in adj:
    for y in fruits:
        if x=="big" and y=="cherry":
            break
        print(x,y)

print("----------------------WHILE----------------------------")

i=0
while i<=10:
    print(i)
    i+=1

i=0
while i<=1000000:
    print(i)
    i+=1
    if i==4:
        break