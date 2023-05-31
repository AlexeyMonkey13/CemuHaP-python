# import csv
# with open("phonebook.csv", encoding='utf-8') as r_file:
#     # Создаем объект reader, указываем символ-разделитель ","
#     file_reader = csv.reader(r_file, delimiter = ",")
#     # Счетчик для подсчета количества строк и вывода заголовков столбцов
#     count = 0
#     # Считывание данных из CSV файла
#     for row in file_reader:
#         if count == 0:
#             # Вывод строки, содержащей заголовки для столбцов
#             print(f'Файл содержит столбцы: {",".join(row)}')
#         else:
#             # Вывод строк
#             print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
#         count += 1
#     print(f'Всего в файле {count} строк.')

# import csv
# with open("phonebook.csv", encoding='utf-8') as r_file:
#     # Создаем объект DictReader, указываем символ-разделитель ","
#     file_reader = csv.DictReader(r_file, delimiter = ",")
#     # Счетчик для подсчета количества строк и вывода заголовков столбцов
#     count = 0
#     # Считывание данных из CSV файла
#     for row in file_reader:
#         if count == 0:
#             # Вывод строки, содержащей заголовки для столбцов
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         # Вывод строк
#         print(f' {row["surname"]} - {row[" name"]} - {row[" phone"]}', end='')
#         print(f' и он родился в {row[" discription"]} году.')
#         count += 1
#     print(f'Всего в файле {count + 1} строк.')

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI', lst})
data.head()