# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
list_len = int(input('Введите количество элементов списка: '))
my_list = []
for i in range(list_len):
    my_list.append(input(f'Введите {i+1}-й элемент списка: '))
print(my_list)
list_item = ''
for i in range(0,list_len-1,2):
    list_item = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = list_item
print(my_list)