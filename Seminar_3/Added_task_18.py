import random

num_count = int(input("Введите количество чисел: "))

my_list = []
for i in range(num_count):
    my_list.append(random.randint(1, 10))
print(my_list)

num_search = int(input("Какое число будем искать?: "))

my_list.append(num_search)
my_list.sort()
print(my_list)

if my_list.index(num_search) == 0:
    print(f"Ближайшее по значению к искомому число {my_list[1]}")
else:
    my_list.reverse()
    if my_list.index(num_search) == 0:
        print(f"Ближайшее по значению к искомому число {my_list[1]}")
    else:
        if abs(my_list[my_list.index(num_search) - 1] - num_search) < \
                abs(my_list[my_list.index(num_search) + 1] - num_search):
            print(f"Ближайшее по значению к искомому число {my_list[my_list.index(num_search) - 1]}")
        else:
            print(f"Ближайшее по значению к искомому число {my_list[my_list.index(num_search) + 1]}")
