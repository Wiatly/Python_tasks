def calcul(num):
    if num == 1:
        return 1
    else:
        return num + calcul(num - 1)


input_num = int(input(f"Введите число: "))

print(f"Метод пребора:")
print(*[x for x in range(1, input_num + 1)], sep='+', end=" ")
print(f"= {calcul(input_num)}")

print(f"Метод аналитический:")
print(f"{input_num}({input_num}+1)/2 = {input_num * (input_num + 1) / 2}")
