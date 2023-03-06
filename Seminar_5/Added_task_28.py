def calcul(num_low, num_high, count=1):
    if count > num_low:
        return num_high
    else:
        return 1 + calcul(num_low, num_high, count + 1)


input_first = int(input(f"Введите первое число: "))
input_second = int(input(f"Введите второе число: "))

if input_first > input_second:
    summ = calcul(input_second, input_first)
else:
    summ = calcul(input_first, input_second)

print(f"{input_first} + {input_second} = {summ}")
