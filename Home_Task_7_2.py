# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов  проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class clothes:

    def __init__(self, name, size, height):
        self.name = name
        self._size = size
        self._height = height

    @abstractmethod
    def textile_calc(self):
        pass

    @property
    def size(self):
        if self._size < 22:
            self._size = 22
            return self._size
        else:
            return self._size

    @property
    def height(self):
        if self._height < 130:
            self._height = 130
            return self._height
        else:
            return self._height

class coat(clothes):

    def textile_calc(self):
        if self.name == 'coat':
            return round(self._size / 6.5 + 0.5, 2)
        else:
            0

class suit(clothes):

    def textile_calc(self):
        if self.name == 'suit':
            return round(2 * self._height + 0.3, 2)
        else:
            0

coat1 = coat('coat', 12, 128)
print(f'Количество ткани, необходимое для пошива пальто размера {coat1.size}, роста {coat1.height}: {coat1.textile_calc()}')

suit1 = suit('suit', 42, 162)
print(f'Количество ткани, необходимое для пошива пальто размера {suit1.size}, роста {suit1.height}: {suit1.textile_calc()}')