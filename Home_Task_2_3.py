# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
my_dict = {1: 'зима'
     ,2: 'зима'
     ,3: 'весна'
     ,4: 'весна'
     ,5: 'весна'
     ,6: 'лето'
     ,7: 'лето'
     ,8: 'лето'
     ,9: 'осень'
     ,10: 'осень'
     ,11: 'осень'
     ,12: 'зима'
     }
my_list = ['зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']
month = int(input('Введите порядковый номер месяца: '))
print(f'Время года месяца через словарь - {my_dict.get(month)}')
print(f'Время года месяца через список - {my_list[month-1]}')