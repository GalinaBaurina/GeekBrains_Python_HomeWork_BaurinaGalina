#Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
name = input('Введите своё имя: ')
weight = float(input('Введите свой вес: '))
water = float(input('Введите сколько литров воды Вы выпиваете за день: '))
protein = float(input('Введите сколько грам белка Вы съедаете за день: '))
water_norm_index = 0.04
protein_norm_index = 2
print(f'Здравствуй, {name}!')
if weight * water_norm_index > water:
    print(f'Вам нужно пить на {round(weight * water_norm_index - water,2)} литров воды в день больше')
elif weight * water_norm_index < water:
    print(f'Вам можно пить на {round(water - weight * water_norm_index ,2)} литров воды в день меньше')
else:
    print(f'Вы пьёте достаточное количество воды')

if weight * protein_norm_index > protein:
    print(f'Вам нужно есть на {round(weight * protein_norm_index - protein,2)} грам белка в день больше')
elif weight * protein_norm_index < protein:
    print(f'Вам можно есть на {round(protein - weight * protein_norm_index,2)} грам белка в день меньше')
else:
    print(f'Вы едите достаточное количество белка')
