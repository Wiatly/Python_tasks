import random

num_count_1 = int(input("Введите количество чисел первого массива: "))
num_count_2 = int(input("Введите количество чисел второго массива: "))

my_list_1 = []
for i in range(num_count_1):
    my_list_1.append(random.randint(1, 10))
print(my_list_1)

my_list_2 = []
i=0
for i in range(num_count_2):
    my_list_2.append(random.randint(1, 10))
print(my_list_2)

my_list_1 = set(my_list_1)
my_list_2 = set(my_list_2)

my_list_3 = my_list_1.intersection(my_list_2)
my_list_3=list(my_list_3)
my_list_3.sort()
print(my_list_3)
