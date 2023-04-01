"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json

def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    with open('orders.json') as json_file:
         data_all = json.load(json_file)
         data_new=data_all['orders']
         data_new.append(data)
         data_all.update(orders=data_new)
         print(data_all)

    with open('orders_out.json', 'w') as write_json:
        json.dump(data_all, write_json, indent=4)


write_order_to_json(
    item='monitor',
    quantity=5,
    price=100.00,
    buyer='Petrov P.P.',
    date='10.10.2020')