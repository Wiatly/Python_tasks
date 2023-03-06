def calcul(num):
    global even, odd
    if num == 0:
        return
    else:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    calcul(num // 10)


num = int(input("Введите число: "))

even = odd = 0
calcul(num)
print(f"Количество нечетных цифр {odd}, четных {even}")
