# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб)
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

f = open('file_5_6.txt', 'r')
subject_list = []
lecture_list = []
practice_list = []
laboratory_list = []

for line in f:
    subject_list.append(line.split()[0])
    lecture_list.append(line.split()[1])
    practice_list.append(line.split()[2])
    laboratory_list.append(line.split()[3])
f.close()

clean_subject_list = [subject[0:subject.find(':')] for subject in subject_list]
clean_lecture_list = [0 if lecture[0:lecture.find('(')] == '' else int(lecture[0:lecture.find('(')]) for lecture in lecture_list]
clean_practice_list = [0 if practice[0:practice.find('(')] == '' else int(practice[0:practice.find('(')]) for practice in practice_list]
clean_laboratory_list = [0 if laboratory[0:laboratory.find('(')] == '' else int(laboratory[0:laboratory.find('(')]) for laboratory in laboratory_list]

subject_hour_list = []
for i in range(len(clean_subject_list)):
    subject_hour_list.append(clean_lecture_list[i] + clean_practice_list[i] + clean_laboratory_list[i])

subject_hour_dict = dict(zip(clean_subject_list, subject_hour_list))
print(f'Название предмета и общее количество занятий по нему:\n{subject_hour_dict}')