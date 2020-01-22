# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

f = open('file_5_5.txt', 'w')
digit_line = input('Введите через пробел числа: ')
f.write(digit_line)
digit_list = [int(digit) for digit in digit_line.split()]
print(f'Сумма чисел в файле: {sum(digit_list)}')
f.close()