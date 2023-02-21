ticket_num = input("Введите шестизначный номер билета: ")

sum_first_three_digit=int(ticket_num[0])+int(ticket_num[1])+int(ticket_num[2])
sum_last_three_digit=int(ticket_num[3])+int(ticket_num[4])+int(ticket_num[5])

if sum_first_three_digit==sum_last_three_digit:
    print(f"Билет с этим номером счастливый")
else:
    print(f"Билет с этим номером несчастливый")
