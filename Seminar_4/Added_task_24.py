import random

num_count = int(input("Введите количество кустов: "))

my_list = []
for i in range(num_count):
    my_list.append(random.randint(1, 100))
print(my_list)

my_list.append(my_list[0])
my_list.append(my_list[1])
print(my_list)

max_ber = 0
for i in range(1, len(my_list) - 1):
    if max_ber < my_list[i - 1] + my_list[i] + my_list[i + 1]:
        max_ber = my_list[i - 1] + my_list[i] + my_list[i + 1]

print(max_ber)
