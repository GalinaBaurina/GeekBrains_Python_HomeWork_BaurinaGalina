# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class cell:

    def __init__(self, subcell_cnt):
        self.subcell_cnt = subcell_cnt

    def __add__(self,other):
        new_cell = cell(self.subcell_cnt + other.subcell_cnt)
        return new_cell

    def __sub__(self,other):
        if self.subcell_cnt > other.subcell_cnt:
            new_cell = cell(self.subcell_cnt - other.subcell_cnt)
            return new_cell
        else:
            print('Ошибка! У первой клетки количество ячеек должно быть больше, чем у второй')
            return cell(0)

    def __mul__(self,other):
        new_cell = cell(self.subcell_cnt * other.subcell_cnt)
        return new_cell

    def __truediv__(self,other):
        if other.subcell_cnt != 0:
            new_cell = cell(int(self.subcell_cnt / other.subcell_cnt))
            return new_cell
        else:
            print('Ошибка! У второй клетки количество ячеек должно быть больше нуля')
            return cell(0)

    def make_order(self, row_subcell_cnt):
        full_row_cnt = self.subcell_cnt // row_subcell_cnt
        last_row_subcell_cnt = self.subcell_cnt % row_subcell_cnt
        subcell_str = ''
        for i in range(full_row_cnt):
            j = 0
            for j in range(row_subcell_cnt):
                subcell_str = subcell_str + '*'
            subcell_str = subcell_str + '\n'
        for k in range(last_row_subcell_cnt):
            subcell_str = subcell_str + '*'
        return subcell_str


c1 = cell(int(input('Введите количество ячеек в клетке 1: ')))
c2 = cell(int(input('Введите количество ячеек в клетке 2: ')))
c3 = c1 + c2
print(f'Количество ячеек в новой клетке, получившейся в результате сложения двух клеток: {c3.subcell_cnt}')
c4 = c1 - c2
print(f'Количество ячеек в новой клетке, получившейся в результате вычитания двух клеток: {c4.subcell_cnt}')
c5 = c1 * c2
print(f'Количество ячеек в новой клетке, получившейся в результате умножения двух клеток: {c5.subcell_cnt}')
c6 = c1 / c2
print(f'Количество ячеек в новой клетке, получившейся в результате деления двух клеток: {c6.subcell_cnt}')
row_subcell_cnt_1 = int(input('Введите количество ячеек в одном ряду для клетки 1: '))
print(f'Распределение ячеек по рядам для клетки 1:\n{c1.make_order(row_subcell_cnt_1)}')