first_el = int(input("Введите первый элемент : "))
count_el = int(input("Введите количество элементов : "))
div_el = int(input("Разность : "))

new_list = [first_el + el* div_el for el in range(count_el)]

print(new_list)
