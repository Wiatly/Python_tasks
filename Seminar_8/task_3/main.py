"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

first_dict_element = [
    'First element',
    'Second element',
    'Third element',
    'Tourth element',
]

second_dict_element = 888

third_dict_element = {
    'First element':  str(100) + u'\u00A3',
    'Second element': str(200) + u'\u00A3',
    'Third element': str(300) + u'\u00A3',
}

to_yaml = {'first_key': first_dict_element, 'second_key': second_dict_element, 'third_key': third_dict_element}

with open('test.yaml', 'w', encoding='utf-16') as t_f:
    yaml.dump(to_yaml, t_f, allow_unicode=True, default_flow_style=False, default_style='"')

with open('test.yaml', 'r', encoding='utf-16') as file_read:
    print(yaml.safe_load(file_read) == to_yaml)