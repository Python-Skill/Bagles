# Боже что это за говнокод( зато мой:) )
from random import randint 

print("Я загад 3-значное число.Попробуйте угадать какое именно.")
print("Вот несколько подсказок:")
print("Когда я говорю:         Я имею ввиду:")
print("Pico                    Одна цифра верна,но находиться не на своей позиции")
print("Fermi                   Одна цифра верна и находится на своей позиции")
print("Bagels                  Не одна цифра не являеться правильной")
print()
print("У вас есть 10 попыток,чтобы угадачть заданное число!")

# Генератор рандомного числа
a = randint(100, 999)
numberan = str(a)
print(a)
# Цикл котрый запустит ввод 10раз
for b in range(1, 10):
    numbervd = input()

    if int(numbervd) == int(numberan):
        print("Вы угадали заданное число")
        break

    # Цикл првоерки введина ли бы хотябы одна цифра правельно и находиться ли она на своем месте
    for i in range(0, 3):
        if int(numbervd[i]) == int(numberan[i]):
            print("Fermi")
            break
        else:
            print("Bagels")
            break

    # Цикл првоерки введина ли бы хотябы одна цифра правельно и находиться ли она не на своем месте
    for n in range(0, 3):
        for v in range(0, 3):
            if int(numbervd[n]) == int(numberan[v]):
                print("Pico")
                break
    
    # Хуйня не работает
    if b > 9:
        print("Вы не угадали заданное число")