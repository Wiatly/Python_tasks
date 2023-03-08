from random import randint

new_list = []

for i in range(20): new_list.append(randint(0, 9))
print(new_list)

new_list_1 = list(enumerate(new_list))

for i in range(len(new_list_1)):
    if 3 <= new_list_1[i][1] <= 4:
        print(i)
