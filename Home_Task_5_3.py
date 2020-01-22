# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

f = open('file_5_3.txt', 'r')
employee_list = []
salary_list = []
line_num = 0
salary_sum = 0
print('Сотрудники, которые получают меньше 20000: ')
for line in f:
    employee_list.append(line.split()[0])
    salary_list.append(float(line.split()[1]))
    if salary_list[line_num] < 20000:
        print(employee_list[line_num])
    line_num = line_num + 1
print(f'Средняя величина дохода сотрудников: {round(sum(salary_list)/len(salary_list),2)}')
f.close()