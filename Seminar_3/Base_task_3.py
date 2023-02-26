# Заполненный список
# goods = [
#     (1, {"название": "Газета", "цена": 40, "количество": 19, "eд": "пачка"}),
#     (2, {"название": "Журнал", "цена": 100, "количество": 10, "eд": "шт"}),
#     (3, {"название": "Открытка", "цена": 10, "количество": 100, "eд": "шт"})
# ]

goods = []
n = 1
goods_count = int(input("Введите количество товаров: "))
for i in range(goods_count):
    print(f"Задайте данные по {i + 1}-му товару")
    goods_name = input("Название: ")
    goods_price = int(input("Цена: "))
    goods_count = int(input("Количество: "))
    goods_measure = input("Единица измерения: ")
    goods.append((i + 1, {"название": goods_name, "цена": goods_price, "количество": goods_count, "eд": goods_measure}))

print(f"Исходный список товаров:")
for i in range(len(goods)):
    print(f"{goods[i]}")

goods_names = []
goods_prices = []
goods_counts = []
goods_measures = []
for i in goods:
    goods_names.append(i[1].get("название"))
    goods_prices.append(i[1].get("цена"))
    goods_counts.append(i[1].get("количество"))
    goods_measures.append(i[1].get("eд"))

report = {
    "название": list(goods_names),
    "цена": list(goods_prices),
    "количество": list(goods_counts),
    "eд": list(goods_measures)
}

print(f"\nАналитика:")
for key, value in report.items():
    print(f"{key[:20]:>20}: {value}")
