def calcul(num, num_pow):
    if num_pow == 1:
        return num
    else:
        return num * calcul(num, num_pow - 1)


input_num = int(input(f"Введите число: "))
input_pow = int(input(f"Введите степень: "))

print(f"{input_num} в степени {input_pow} равно {calcul(input_num, input_pow)}")
