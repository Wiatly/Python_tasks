
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


new_person = Position('Belinda', 'Carlisle', 'singer', 1000, 5000000)
print(f'Установленные атрибуты: {new_person.name}, {new_person.surname}, {new_person.position}, {new_person._income}')
print(f'Суммарный доход {new_person.get_full_name()} составляет {new_person.get_total_income()}')
