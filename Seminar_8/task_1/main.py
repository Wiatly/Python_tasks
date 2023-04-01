"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv
import re
import glob

def write_to_csv(file, data):
    with open(file, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for nrow in data:
            f_n_writer.writerow(nrow)


def get_data(lst):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    print(main_data[0][1])
    for file in lst:
        datafile = open(file)
        for row in datafile:
            row = row.rstrip()
            if re.match(main_data[0][0], row):
                reg_word = re.compile(r'Изготовитель системы:\s*\S*')
                os_prod_list.append(reg_word.findall(row)[0].split()[2])
            elif re.match(main_data[0][1], row):
                reg_word = re.compile(r'Название ОС:\s*\S*')
                os_name_list.append(reg_word.findall(row)[0].split()[2])
            elif re.match(main_data[0][2], row):
                reg_word = re.compile(r'Код продукта:\s*\S*')
                os_code_list.append(reg_word.findall(row)[0].split()[2])
            elif re.match(main_data[0][3], row):
                reg_word = re.compile(r'Тип системы:\s*\S*')
                os_type_list.append(reg_word.findall(row)[0].split()[2])

    for k in range(len(lst)):
        main_data.append([k + 1,
                          os_prod_list[k],
                          os_name_list[k],
                          os_code_list[k],
                          os_type_list[k]
                          ])
    return main_data


res = get_data(glob.glob('*.txt'))
write_to_csv('new_file.csv', res)

with open('new_file.csv') as f_n:
    print(f_n.read())
