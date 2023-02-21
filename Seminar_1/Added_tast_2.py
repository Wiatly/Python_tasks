three_digit = int(input("Задайте трёхзначное число: "))

print(f"Сумма цифр этого числа равна "
      f"{three_digit // 100 + (three_digit - three_digit // 100 * 100) // 10 + three_digit % 10 % 10} = "
      f"({three_digit // 100} + {(three_digit - three_digit // 100 * 100) // 10} + {three_digit % 10 % 10})")
