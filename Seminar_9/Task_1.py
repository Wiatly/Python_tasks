# Сделано два дискриптора для одного класса



import time


class Colors:

    def __set__(self, instance, value):
        if value not in ['красный', 'желтый', 'зеленый']:
            print("Неправильно задан цвет, цвет установлен на Красный")
            instance.__dict__[self.my_attr] = 'красный'
        else:
            instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Is_digit:
    def __set__(self, instance, value):
        if  not value.isdigit():
            print("Вы ввели не число. Время действия сигнала Красный установлено на 3 сек")
            instance.__dict__[self.my_attr] = 3
        else:
            instance.__dict__[self.my_attr] = int(value)

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr



class TrafficLight:

    color = Colors()
    red_delay=Is_digit()

    # время ожидания цветов
    yellow_delay = 1
    green_delay = 1

    # Определяем названия цветов сигналов светофора
    red_name = 'красный'
    yellow_name = 'желтый'
    green_name = 'зеленый'

    def __init__(self, color,red_delay):
        self.color = color
        self.red_delay = red_delay


    def light_change(self, color, wait_time):
        self.wait_time = wait_time
        print(f'На светофоре {color} свет, ждите {self.wait_time} сек')
        time.sleep(self.wait_time)

    # Определяем публичный метод
    def running(self, color='',red_delay=None):
        if not color:
            loc_color = self.color
        else:
            loc_color = color

        if not red_delay:
            red_delay = self.red_delay
        else:
            red_delay = red_delay
            # red_delay = self.red_delay


        if loc_color == self.red_name:
            self.light_change('красный', self.red_delay)
            self.light_change('желтый', self.yellow_delay)
            self.light_change('зеленый', self.green_delay)
        elif loc_color == self.yellow_name:
            self.light_change('желтый', self.yellow_delay)
            self.light_change('зеленый', self.green_delay)
        else:
            self.light_change('зеленый', self.green_delay)


pp=input("Введите начальный цвет светофора:'красный' либо 'желтый' либо 'зеленый' :" )
red_delay=input("Введите время задержки цвета 'красный' :" )
traffic_light_start = TrafficLight(pp,red_delay)
traffic_light_start.running()
