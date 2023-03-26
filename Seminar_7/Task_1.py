import time


class TrafficLight():
    # время ожидания цветов
    red_delay = 7
    yellow_delay = 2
    green_delay = 5

    # Определяем названия цветов сигналов светофора
    red_name = 'красный'
    yellow_name = 'желтый'
    green_name = 'зеленый'

    def __init__(self, color):
        self.__color = color

    def light_change(self, color, wait_time):
        self.wait_time = wait_time
        print(f'На светофоре {color} свет, ждите {self.wait_time} сек')
        time.sleep(self.wait_time)

    # Определяем публичный метод
    def running(self, color=''):
        self.light_change('красный', self.red_delay)
        self.light_change('желтый', self.yellow_delay)
        self.light_change('зеленый', self.green_delay)


traffic_light_start = TrafficLight('красный')
traffic_light_start.running()
