my_list = [7, 5, 3, 3, 2]
print(f"Старый рейтинг : {my_list}")

try:
    new_num = int(input("Введите новое значение в рейтинг: "))
except:
    print(f"Это не число")
else:
    my_list.append(new_num)
    my_list.sort(reverse=True)
    print(f"Новый рейтинг  : {my_list}")
