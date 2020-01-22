# Создать текстовый файл (не программно), сохранить в нем несколько строк.
# Выполнить подсчет количества строк, количества слов в каждой строке.

f = open('file_5_2.txt', 'r')
line_cnt = 0
for line in f:
    line_cnt = line_cnt + 1
    print(f'Количество слов в строке {line_cnt}: {len([word for word in line.split()])}')
print(f'Количество строк в файле: {line_cnt}')
f.close()