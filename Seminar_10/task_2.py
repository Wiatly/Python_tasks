"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

var = [b'class', b'function', b'method']

for line in var:
    print('содержание переменной - {}'.format(line))
    print('тип переменной: {}'.format(type(line)))
    print('длинна строки: {}\n'.format(len(line)))
