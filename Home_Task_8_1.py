# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class dt:

    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = dd_mm_yyyy

    @classmethod
    def dd_mm_yyyy_to_int(cls):
        dd = int(cls.dd_mm_yyyy[0:1])
        mm = int(cls.dd_mm_yyyy[3:4])
        yyyy = int(cls.dd_mm_yyyy[6:9])
        return yyyy

    @staticmethod
    def dd_mm_yyyy_valid(dd_mm_yyyy):
        error_flg = 0
        if int(dd_mm_yyyy[0:2]) < 1 or int(dd_mm_yyyy[0:2]) > 31:
            print('День месяца должен быть от 1 до 31')
            error_flg = 1
        if int(dd_mm_yyyy[3:5]) < 1 or int(dd_mm_yyyy[3:5]) > 12:
            print('Месяц должен быть от 1 до 12')
            error_flg = 1
        if int(dd_mm_yyyy[6:10]) < 1 or int(dd_mm_yyyy[6:10]) > 2020:
            print('Год должен быть от 1 до 2020')
            error_flg = 1
        if error_flg == 0:
            print('Дата введена верно')

dt.dd_mm_yyyy_valid('49_12_2021')
dt.dd_mm_yyyy_valid('19_12_2020')