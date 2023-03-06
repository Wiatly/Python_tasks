def calcul(num, new_num=''):
    if num / 10 < 1:
        return new_num + str(num)
    else:
        new_num = new_num + calcul(num // 10, str(num % 10))
        return new_num


num = int(input("Введите число: "))
print(calcul(num))
