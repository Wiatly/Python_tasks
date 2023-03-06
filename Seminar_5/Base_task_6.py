def calcul(num, count=10):
    input_num = int(input(f"Попытка № {count}. Введите число: "))
    if count == 1:
        print(f"Число попыток закончилось. Загаданное число {num}")
        return
    elif input_num == num:
        print(f"Вы угадали число. Загаданное число {num}")
        return
    elif input_num > num:
        print(f"Введенное число больше загаданного")
        calcul(num, count - 1)
    elif input_num < num:
        print(f"Введенное число меньше загаданного")
        calcul(num, count - 1)


import random

random_integer = random.randint(0, 100)
print(random_integer)
calcul(random_integer)
