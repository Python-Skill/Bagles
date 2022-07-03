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

b = 0 
while b < 10:
    numbervd = input()
    i = 0
    while i < 3:
        if int(numbervd[i]) == int(numberan[i]):
            print("Fermi")
        i +=1

    d = 0
    c = 0
    while c < 3:
        if int(numbervd[d+=1]) == int(numberan[c]):
            print("Pico")
        c +=1

   # f = 0
   # while f < 3:
   #     if int(numbervd[0]) != int(numberan[f]):
   #         print("Bagels")
   #     f +=1
    



 



