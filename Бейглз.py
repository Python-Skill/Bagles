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
print(numberan[1])
b = a // 100    #деление сотен без остатка
c = (a % 100)//10   #десятки
d = a % 10  #единицы

numbervd = input()
print(numbervd[1])


 



