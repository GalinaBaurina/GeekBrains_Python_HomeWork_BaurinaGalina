# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class warehouse:
    def __init__(self):
        pass

class equipment:
    def __init__(self, *params):
        self.name = params[0]
        self.brand = params[1]
        self.model = params[2]
        self.color = params[3]
        self.max_format = params[4]
        self.interface =  params[5]
        self.printing_technology = params[6]
        self.location = params[7]

    def replace(self,location):
        self.location = location

class printer(equipment):
    def __init__(self, *params):
        super().__init__(self, *params)
        self.two_side_printing = params[8]

class scanner(equipment):
    def __init__(self, *params):
        super().__init__(self, *params)
        self.email_sending = params[8]

class xerox(equipment):
    def __init__(self, *params):
        super().__init__(self, *params)
        self.xerox_speed = params[8]


p = printer('HP LaserJet Pro M15w', 'HP', 'LaserJet Pro M15w', 'white', 'A4', 'Wi-Fi, USB', 'лазерная', 'Склад','есть')
print(p.two_side_printing)
print(p.location)
p.replace('Офис 7')
print(p.location)

s = scanner('Canon CanoScan LiDE 300', 'Canon', 'CanoScan LiDE 300', 'black', 'A4', 'Wi-Fi, USB', 'лазерная', 'Офис 4','есть')
print(s.email_sending)
print(s.location)

x = xerox('Xerox B205', 'Xerox', 'B205', 'gray', 'A2', 'Wi-Fi, Ethernet (RJ-45), USB', 'лазерная', 'Офис 1','30 копий в мин')
print(x.xerox_speed)