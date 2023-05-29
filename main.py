from random import randint
a = randint(0,15)
b = False
print(a)
while not b:
    c = int(input("Введите число: "))
    if c == a:
        print("Пабеда")
        break
    else:
        print("GG")

