coin_count = int(input("Введите количество монет : "))

heads_count = 0
tails_count = 0

for i in range(coin_count):
    answer_c = int(input(f"Если монета {i+1} лежит орлом вверх, нажмите 1. Если решкой нажмите 0: "))
    if answer_c == 0:
        heads_count += 1
    else:
        tails_count += 1

if tails_count > heads_count:
    print(heads_count)
else:
    print(tails_count)
