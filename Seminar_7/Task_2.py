class Road():
    # масса асфальта для покрытия одного кв
    # метра дороги асфальтом, толщиной в 1 см в тоннах
    __weight = .025

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Ищем массу асфальта для дороги длиной {self._length} метров и шириной {self._width} метров')

    def road_weight(self, thickness):
        ret_val = self._length * self._width * thickness * self.__weight
        print(f'Масса асфальта, необходимая для покрытия толщиной {thickness} см, равен {ret_val} т')

        return ret_val


road_calc = Road(5000, 20)
weight_calc = road_calc.road_weight(5)
