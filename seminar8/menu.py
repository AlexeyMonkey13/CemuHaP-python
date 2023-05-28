# def show_menu():
#       print("\nВыберите необходимое действие:\n"
#           "1. Отобразить весь справочник\n"
#           "2. найти абонента по имени\n"
#           "3. Найти абонента по фамилии\n"
#           "4. Найти абонента по номеру телефона\n"
#           "5. Добавить абонента в справочник\n"
#           "6. удалить абонента из справочника\n"
#           "7. изменить данные абонента в справочнике"
#           "8. Сохранить справочник в текстовом формате\n"
#           "9. Закончить работу")
#       choice = int(input())
#       return choice

# def parse_csv(filename):
#       results = []
#       fields = ["фамилия", "имя", "телефон", "описание"]
#       with open(filename, 'r', encoding='utf-8') as data:
#             for line in data:
#                   record = dict(zip(fileds, line.strip().split(",")))
#                   results.append(record)
#       return results

# def work_with_phonebook():
#       choice = show_menu()
#       phone_book = parse_csv('phonebook.csv')

#       while (choice != 9):
#             if choice == 1:
#                   print_result(phone_book)
#             elif choice == 2:
#                   name = get_search_name()
#                   print(find_by_name(phone_book))
#             elif choice == 3:
#                   surname = get_search_surname()
#                   print(find_by_surname(phone_book))
#             elif choice == 4:
#                   number = get_search_number()
#                   print(find_by_number(phone_book))
#             elif choice == 5:
#                   user_data = get_new_user()
#                   add_user(phone_book, user_data)
#                   write_csv('phonebook.csv', phone_book)
#             elif choice == 6:
#                   user_data = get_new_user()
#                   dell_user(phone_book, user_data)
#                   write_csv('phonebook.csv', phone_book)
#             elif choice == 7:
#                   change_userdata(phone_book)
#                   rewrite_scv("phonebook.csv", phone_book)
#             elif choice == 8:
#                   file_name = get_file_name()
#                   write_txt(file_name, phone_book)
#       choice = show_menu()

# def show_phonebook(phone_book): #отобразить справочник весь
#       for elem in phone_book:
#             for key in elem:
#                   print(f"{key} : {elem[key]}")
#             print()
# def find_by_name(phone_book): #find name2
#       name = input("enter search sourch name")
#       result = []
#       for elem in phone_book:
#             if elem["name"] == name:
#                   result.append(elem)
#       return result

# def find_by_surname(phone_book): #find surname3
#       name = input("enter search sourch name")
#       result = []
#       for elem in phone_book:
#             if elem["name"] == name:
#                   result.append(elem)
#       return result

# def find_by_name(phone_book): #find phone_number4
#       name = input("enter search sourch surname ")
#       result = []
#       for elem in phone_book:
#             if elem["surname"] == surname:
#                   result.append(elem)
#       return result

# def add_new_user(phone_book): #add user5
#       record = dict()
#       for k in phone_book[0].keys():
#             record[k] = input(f"enter {k}: ")
#       phone_book.append(record)
# def write_csv(filename, phone_book):
#       with open(filename, "a", encoding="utf-8") as data:
#             line = " "
#             for v in phone_book[-1].values():
#                   line += v + ","
#             data.write(f"{line[:-1]}\n")

# def change_userdata(phone_book): #change user7
#       user = input("enter change name or surname ")
#       changed_atr = input("enter atr change ")
#       for elem in phone_book:
#             for v in elem.values:
#                   if v == user:
#                         elem[changed_atr] = elem[changed_atr].replace(elem[changed_atr],new_art)


# def make_txt(): #save txt8
#       filename = input("name for save" )
#       shutil.copyfile("phonebook", f"{filename}.txt")

# import shutil #end9
# work_with_phonebook()


def show_menu():
    print("\nВыберите нужное действие: \n"
          "1.Отобразить весь справочник\n"
          "2.Найти абонента по фамилии\n"
          "3.Найти абонента по номеру\n"
          "4.Добавить абонента\n"
          "5.Удалить абонента\n"
          "6.Сохранить справочник в текстовом формате\n"
          "7.Закончить работу\n")
    choice = int(input())
    return choice

def read_csv(filename:str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_txt(filename:str, data:list):
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ','
            f_out.write(f'{s[:-1]}\n')

def print_result(data:list):
    print('-'*10)
    for elem in data:
        for key in elem:
            print(f"{key} : {elem[key]}")
        print('-'*10)

def get_search_name():
    return input('Фамилия: ')

def find_by_name(data:list, name: str):
    result = []
    for elem in data:
        if elem['Фамилия'] == name:
            result.append(elem)
    return result

def find_by_number(data:list, number: str):
    result = []
    for elem in data:
        if elem['Телефон'] == number:
            result.append(elem)
    return result

def get_new_user():
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, input('Введите фамилию, имя, номер, описание').strip().split(',')))
    return record
    
def add_user(data:list, user:dict):
    return data.append(user)

def write_csv(filename:str, data:list):
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ','
            f_out.write(f'{s[:-1]}\n')

def delete_by_name(data:list, name: str):
    for elem in data:
        if elem['Фамилия'] == name:
            data.remove(elem)
    return data




def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('seminar_08\phonebook.csv')

    while(choice!=7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print_result(find_by_name(phone_book, name))
        elif choice == 3:
            num = input("номер: ")
            print_result(find_by_number(phone_book, num))
        elif choice == 4:
            new_user = get_new_user()
            add_user(phone_book, new_user)
            write_csv('seminar_08\phonebook.csv', phone_book)
        elif choice == 5:
            del_name = get_search_name()
            delete_by_name(phone_book, del_name)
            write_csv('seminar_08\phonebook.csv', phone_book)
        elif choice == 6:
            write_txt('phonebook.txt', phone_book)
        choice = show_menu()

work_with_phonebook()