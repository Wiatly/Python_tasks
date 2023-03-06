def calcul(num):
    if num == 1:
        return 1
    else:
        sum = (-0.5) ** (num - 1) + calcul(num - 1)
        return sum


num = int(input("Введите количество элементов ряда: "))
print(calcul(num))
