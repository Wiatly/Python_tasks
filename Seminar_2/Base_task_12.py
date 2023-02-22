sum_numbers = int(input("Введите сумму чисел : "))
mult_numbers = int(input("Введите призведение чисел : "))
flag = False

for i in range(1000):
    for j in range(1000):
        if i + j == sum_numbers and i * j == mult_numbers:
            print(f"это числа {i} и {j}")
            flag = True
    if flag:
        break
