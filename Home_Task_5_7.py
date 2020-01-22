# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

f = open('file_5_7_1.txt', 'r')
company_list = []
property_list = []
revenue_list = []
cost_list = []
profit_list = []
profit_sum = 0
profit_company_cnt = 0

for line in f:
    company_list.append(line.split()[0])
    property_list.append(line.split()[1])
    revenue_list.append(line.split()[2])
    cost_list.append(line.split()[3])
    profit_list.append(int(line.split()[2]) - int(line.split()[3]))
    if int(line.split()[2]) - int(line.split()[3]) <= 0:
        profit_sum = profit_sum + 0
        profit_company_cnt = profit_company_cnt + 0
    else:
        profit_sum = profit_sum + int(line.split()[2]) - int(line.split()[3])
        profit_company_cnt = profit_company_cnt + 1
f.close()

avg_profit = profit_sum / profit_company_cnt
profit_dict = dict(zip(company_list, profit_list))
avg_profit_dict = {"avg_profit": avg_profit}
final_profit_list = [profit_dict,avg_profit_dict]
print(f'Список прибыли:\n{final_profit_list}')

with open("file_5_7_2.json", "w") as jf:
    json.dump(final_profit_list, jf)

