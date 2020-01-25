# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
# {'полицейская' if Car.is_police = True else ''} {Car.color} {Car.name}
import random

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police

    def go(self):
        car_desc = 'Полицейская ' if Car.is_police == True else ''
        print(f'{car_desc}Машина {Car.color} {Car.name} поехала')
        return 'go'

    def stop(self):
        car_desc = 'Полицейская ' if Car.is_police == True else ''
        print(f'{car_desc}Машина {Car.color} {Car.name} остановилась')
        return 'stop'

    def turn(self, direction):
        car_desc = 'Полицейская ' if Car.is_police == True else ''
        print(f'{car_desc}Машина {Car.color} {Car.name} повернула на{direction}')
        return 'turn'

    def show_speed(self,action):
        if action == 'go':
            Car.speed = random.randint(1, 200)
        elif action == 'stop':
            Car.speed = 0
        else:
            Car.speed = random.randint(1, 60)
        print(f'Текущая скорость - {Car.speed}')

class TownCar(Car):
    def show_speed(self,action):
        if action == 'go':
            TownCar.speed = random.randint(1, 150)
        elif action == 'stop':
            TownCar.speed = 0
        else:
            TownCar.speed = random.randint(1, 40)
        violation = ' - ПРЕВЫШЕНИЕ! ' if TownCar.speed > 60 else ''
        print(f'Текущая скорость - {TownCar.speed} {violation}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self, action):
        if action == 'go':
            WorkCar.speed = random.randint(1, 100)
        elif action == 'stop':
            WorkCar.speed = 0
        else:
            WorkCar.speed = random.randint(1, 30)
        violation = ' - ПРЕВЫШЕНИЕ! ' if WorkCar.speed > 40 else ''
        print(f'Текущая скорость - {WorkCar.speed} {violation}')

class PoliceCar(Car):
    pass

TownCar1 = TownCar(60, 'голубой', 'Ford', False)
TownCar1.show_speed(TownCar1.go())
TownCar1.show_speed(TownCar1.turn('право'))
TownCar1.show_speed(TownCar1.turn('лево'))
TownCar1.show_speed(TownCar1.stop())

SportCar1 = SportCar(180, 'красный', 'Ferrari', False)
SportCar1.show_speed(SportCar1.go())
SportCar1.show_speed(SportCar1.turn('право'))
SportCar1.show_speed(SportCar1.turn('лево'))
SportCar1.show_speed(SportCar1.stop())

WorkCar1 = WorkCar(60, 'оранжевый', 'MAN', False)
WorkCar1.show_speed(WorkCar1.go())
WorkCar1.show_speed(WorkCar1.turn('право'))
WorkCar1.show_speed(WorkCar1.turn('лево'))
WorkCar1.show_speed(WorkCar1.stop())

PoliceCar1 = PoliceCar(60, 'бело-голубая', 'Lada', True)
PoliceCar1.show_speed(PoliceCar1.go())
PoliceCar1.show_speed(PoliceCar1.turn('право'))
PoliceCar1.show_speed(PoliceCar1.turn('лево'))
PoliceCar1.show_speed(PoliceCar1.stop())