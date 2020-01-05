# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = []
my_list.append('Соедините')
my_list.append(2)
my_list.append('белка')
my_list.append('и')
my_list.append(3.5)
my_list.append('ложки')
my_list.append('сахара')
print(my_list)
if type(my_list[0]) == type('строка'):
    print(f'Тип {my_list.index("Соедините")+1}-ого элемента списка - str')
else:
    print(f'Тип {my_list.index("Соедините")+1}-ого элемента списка должен быть str')
if type(my_list[1]) == type(1):
    print(f'Тип {my_list.index(2)+1}-ого элемента списка - int')
else:
    print(f'Тип {my_list.index(2)+1}-ого элемента списка должен быть int')
if type(my_list[2]) == type('строка'):
    print(f'Тип {my_list.index("белка")+1}-ого элемента списка - str')
else:
    print(f'Тип {my_list.index("белка")+1}-ого элемента списка должен быть str')
if type(my_list[3]) == type('строка'):
    print(f'Тип {my_list.index("и")+1}-ого элемента списка - str')
else:
    print(f'Тип {my_list.index("и")+1}-ого элемента списка должен быть str')
if type(my_list[4]) == type(0.1):
    print(f'Тип {my_list.index(3.5)+1}-ого элемента списка - float')
else:
    print(f'Тип {my_list.index(3.5)+1}-ого элемента списка должен быть float')
if type(my_list[5]) == type('строка'):
    print(f'Тип {my_list.index("ложки")+1}-ого элемента списка - str')
else:
    print(f'Тип {my_list.index("ложки")+1}-ого элемента списка должен быть str')
if type(my_list[0]) == type('строка'):
    print(f'Тип {my_list.index("сахара")+1}-ого элемента списка - str')
else:
    print(f'Тип {my_list.index("сахара")+1}-ого элемента списка должен быть str')

