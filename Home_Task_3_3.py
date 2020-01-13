# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(arg1, arg2, arg3):
    my_list = []
    my_list.append(arg1)
    my_list.append(arg2)
    my_list.append(arg3)
    max_arg = max(my_list)
    min_arg = min(my_list)
    arg_sum = 0
    k = 0
    for i in range(len(my_list)):
        if my_list[i] != min_arg:
            arg_sum = arg_sum + my_list[i]
            k = k + 1
    if k == 2:
        return arg_sum
    elif k == 1:
        return arg_sum + min_arg
    else:
        return 2 * min_arg

a1 = int(input('Введите первое число: '))
a2 = int(input('Введите второе число: '))
a3 = int(input('Введите третье число: '))
print(f'Сумма двух максимальных чисел = {my_func(a1, a2, a3)}')

