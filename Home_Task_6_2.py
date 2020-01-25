# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        Road._length = length
        Road._width = width

    def asphalt_mass(self, depth, mass):
        return Road._length * Road._width * depth * mass
l = int(input('Введите длину дорожного полотна в м: '))
w = int(input('Введите ширину дорожного полотна в м: '))
d = int(input('Введите толщину дорожного полотна в см: '))
m = int(input('Введите массу асфальта, необходимого для покрытия 1 кв.м толщиной 1 см: '))

Road1 = Road(l,w)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {Road1.asphalt_mass(d,m)}')