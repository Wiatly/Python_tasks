num = int(input("Введите число : "))
n = 0

while 2 ** n <= num:
    print(f"{2 ** n}")
    n += 1
