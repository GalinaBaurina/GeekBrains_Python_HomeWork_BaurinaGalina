# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def list_sum(digit_list):
    result = 0
    for k in digit_list:
        result = result + int(k)
    print(f'Сумма всех элементов списка: {result}')
    return result

my_list = []
while True:
    my_string = input('Введите через пробел числа: ')
    my_list_buf = my_string.split(' ')
    my_list = my_list + my_list_buf
    if my_string.find('f') == -1:
        print(f'Все элементы списка: {my_list}')
        list_sum(my_list)
    else:
        break
