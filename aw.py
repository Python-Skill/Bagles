from random import randint #Боже что это за говнокод

print("Я загад 3-значное число.Попробуйте угадать какое именно.")
print("Вот несколько подсказок:")
print("Когда я говорю:         Я имею ввиду:")
print("Pico                    Одна цифра верна,но находиться не на своей позиции")
print("Fermi                   Одна цифра верна и находится на своей позиции")
print("Bagels                  Не одна цифра не являеться правильной")
print()
print("У вас есть 10 попыток,чтобы угадачть заданное число!")

a = randint(100, 999)   #генератор рандомного числа
numberan = str(a)
print(a)

for b in range(1, 10):
    numbervd = input()
    i = 0
    for i in range(0, 3):
        if int(numbervd[i]) == int(numberan[i]):
            print("Fermi")

    for n in range(0, 3):
        for v in range(0, 3):
            if int(numbervd[n]) == int(numberan[v]):
                print("Pico")
    else:
        print("Bagels")

    

