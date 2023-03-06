def calcul():
    operand = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if operand in ("0", "+", "-", "*", "/"):
        if operand == "0":
            return
        else:
            first_num = input("Введите первое число: ")
            second_num = input("Введите второе число: ")
            if first_num.isdigit() and second_num.isdigit():
                if operand == "/" and second_num == "0":
                    print(f"На 0 делить нельзя")
                    calcul()
                else:
                    print(eval(first_num + operand + second_num))
                    calcul()
            else:
                print(f"Это не число")
                calcul()
    else:
        print(f"Это не знак операции")
        calcul()


calcul()
