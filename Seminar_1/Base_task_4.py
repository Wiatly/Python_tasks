sell_value = int(input("Задайте сумму выручки: "))
cost_value = int(input("Задайте сумму издержек: "))

if sell_value > cost_value:
    print(f"Финансовый результат - прибыль. Ее величина: {sell_value - cost_value}")
    print(f"Рентабельность выручки =  {(sell_value - cost_value) / sell_value}")
    employee_count = int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника = {(sell_value - cost_value) / employee_count}")
else:
    print(f"Прибыли нет")
