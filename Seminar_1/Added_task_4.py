crane_count = int(input("Введите количество журавликов: "))

if crane_count % 6 == 0:
    print(f"Петя и Сережа сделали по {int(crane_count / 6)} журавликов. Катя сделала {int(crane_count / 6 * 4)}"
          f" журавликов.")
else:
    print(f"Целочисленного решения нет")
