first_el = int(input("Введите первый элемент : "))
count_el = int(input("Введите количество элементов : "))
div_el = int(input("Разность : "))

new_list = [first_el + (el-first_el) / div_el for el in range(first_el, first_el + count_el)]

print(new_list)
