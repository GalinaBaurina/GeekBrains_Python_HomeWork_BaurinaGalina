# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income["wage"] = wage
        Worker._income["bonus"] = bonus

class Position(Worker):
    def get_full_name(self):
        return Position.name + ' ' + Position.surname

    def get_total_income(self):
        return Position._income["wage"] + Position._income["bonus"]

manager = Position('Vasya','Petrov', 'manager', 35000, 15000)
print(manager.get_full_name())
print(manager.get_total_income())

analyst = Position('Klava','Ivanova', 'analyst', 25000, 10000)
print(analyst.get_full_name())
print(analyst.get_total_income())