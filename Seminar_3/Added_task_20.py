my_list = [("A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"),
           ("D", "G", "Д", "К", "Л", "М", "П", "У"),
           ("B", "C", "M", "P","Б", "Г", "Ё", "Ь", "Я"),
           ("F", "H", "V", "W", "Y","Й", "Ы"),
           ("K", "Ж", "З", "Х", "Ц", "Ч"),
           (),
           (),
           ("J", "X","Ш", "Э", "Ю"),
           (),
           ("Q", "Z","Ф", "Щ", "Ъ")]

enumNames = list(enumerate(my_list,start=1))

input_word = input("Введите слово: ")
input_word = input_word.upper()

sum = 0
for i in range(len(input_word)):
    for j in range(len(enumNames)):
        sum=sum+enumNames[j][1].count(input_word[i])*enumNames[j][0]

print(f"Стоимость слова : {sum}")