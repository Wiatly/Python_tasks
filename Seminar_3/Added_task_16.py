import random

num_count = int(input("Введите количество чисел: "))

my_list = []
for i in range(num_count):
    my_list.append(random.randint(1, 10))
print(my_list)

num_search = int(input("Какое число будем считать?: "))

print(f"Количество элементов {num_search}: {my_list.count(num_search)}")
