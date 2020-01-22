# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f1 = open('file_5_4_1.txt', 'r')
eng_word_list = []
rus_word_list = []
digit_list = []
line_num = 0
for line in f1:
    eng_word_list.append(line.split()[0])
    digit_list.append(int(line.split()[2]))
    if eng_word_list[line_num].lower() == 'one':
        rus_word_list.append('Один - 1\n')
    elif eng_word_list[line_num].lower() == 'two':
        rus_word_list.append('Два - 2\n')
    elif eng_word_list[line_num].lower() == 'three':
        rus_word_list.append('Три - 3\n')
    elif eng_word_list[line_num].lower() == 'four':
        rus_word_list.append('Четыре - 4\n')
    elif eng_word_list[line_num].lower() == 'five':
        rus_word_list.append('Пять - 5\n')
    elif eng_word_list[line_num].lower() == 'six':
        rus_word_list.append('Шесть - 6\n')
    elif eng_word_list[line_num].lower() == 'seven':
        rus_word_list.append('Семь - 7\n')
    elif eng_word_list[line_num].lower() == 'eight':
        rus_word_list.append('Восемь - 8\n')
    elif eng_word_list[line_num].lower() == 'nine':
        rus_word_list.append('Девять - 9\n')
    elif eng_word_list[line_num].lower() == 'ten':
        rus_word_list.append('Десять - 10\n')
    line_num = line_num + 1
f1.close()

f2 = open('file_5_4_2.txt', 'w')
f2.writelines(rus_word_list)
f2.close()