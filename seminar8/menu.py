def show_menu():
    print("\nВыберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. найти абонента по имени\n"
        "3. Найти абонента по фамилии\n"
        "4. Найти абонента по номеру телефона\n"
        "5. Добавить абонента в справочник\n"
        "6. удалить абонента из справочника\n"
        "7. изменить данные абонента в справочнике"
        "8. Сохранить справочник в текстовом формате\n"
        "9. Закончить работу")
    choice = int(input())
    return choice

def parse_csv(filename):
    results = []
    fields = ["surname", "name", "phone", "discription"]
    with open (filename, 'r', encoding='utf-8') as data:
            for line in data:
                record = dict(zip(fields, line.strip().split(',')))
                results.append(record)
    return results

def work_with_phonebook():
    choice = show_menu()
    phone_book = parse_csv('phonebook.csv')

    while (choice != 9):
        if choice == 1:
            show_phonebook(phone_book)
            enter = input("нажми ентер для продолжения ...") 
        elif choice == 2:
            show_phonebook(find_by_name(phone_book))
            enter = input("нажми ентер для продолжения ...")
        elif choice == 3:
            show_phonebook(find_by_surname(phone_book))
            enter = input("нажми ентер для продолжения ...")
        elif choice == 4:
            show_phonebook(find_by_phone(phone_book))
            enter = input("нажми ентер для продолжения ...")
        elif choice == 5:
            add_new_user(phone_book)
            write_csv("phonebook.csv", phone_book)
        elif choice == 6:
            delete_user(phone_book)
            write_csv('phonebook.csv', phone_book)
        elif choice == 7:
            change_userdata(phone_book)
            rewrite_scv("phonebook.csv", phone_book)
        elif choice == 8:
            make_txt()
        choice = show_menu()

def show_phonebook(phone_book): #отобразить справочник весь
    for elem in phone_book:
        for key in elem:
            print(f'{key} : {elem[key]}')
        print()

def find_by_name(phone_book): #find name2
      name = input("enter search sourch name")
      result = []
      for elem in phone_book:
            if elem["name"] == name:
                  result.append(elem)
      return result

def find_by_surname(phone_book): #find surname3
      name = input("enter search sourch name")
      result = []
      for elem in phone_book:
            if elem["surname"] == surname:
                  result.append(elem)
      return result

def find_by_number(phone_book): #find phone_number4
      name = input("enter search sourch surname ")
      result = []
      for elem in phone_book:
            if elem["phone"] == number:
                result.append(elem)
      return result

def add_new_user(phone_book): #add user5
      record = dict()
      for k in phone_book[0].keys():
            record[k] = input(f"enter {k}: ")
      phone_book.append(record)

def write_csv(filename, phone_book):
      with open(filename, "a", encoding="utf-8") as data:
            line = " "
            for v in phone_book[-1].values():
                  line += v + ","
            data.write(f"{line[:-1]}\n")

def delete_user(phone_book):
    user = input("введите удаляйщика")
    for elem in phone_book:
        for v in elem.values():
            if v == user:
                phone_book.remove(elem)

def write_csv(filename, phone_book):
    with open(filename, "w", encoding="utf-8") as data:
        for i in range(len(phone_book)):
            line = ''
            for v in phone_book[i].values():
                line += v + ','
            data.write(f"{line[:-1]}\n")

def change_userdata(phone_book): #change user7
      user = input("enter change name or surname ")
      changed_atr = input("enter atr change ")
      for elem in phone_book:
            for v in elem.values():
                  if v == user:
                        elem[changed_atr] = elem[changed_atr].replace(elem[changed_atr],new_art)


def make_txt(): #save txt8
      filename = input("name for save" )
      shutil.copyfile("phonebook", f"{filename}.txt")

import shutil #end9
work_with_phonebook()


# def show_menu():
#     print("\nВыберите нужное действие: \n"
#           "1.Отобразить весь справочник\n"
#           "2.Найти абонента по фамилии\n"
#           "3.Найти абонента по номеру\n"
#           "4.Добавить абонента\n"
#           "5.Удалить абонента\n"
#           "6.Сохранить справочник в текстовом формате\n"
#           "7.Закончить работу\n")
#     choice = int(input())
#     return choice

# def read_csv(filename:str):
#     data = []
#     fields = ["Фамилия", "Имя", "Телефон", "Описание"]
#     with open(filename, 'r', encoding='utf-8') as fin:
#         for line in fin:
#             record = dict(zip(fields, line.strip().split(',')))
#             data.append(record)
#     return data

# def write_txt(filename:str, data:list):
#     with open(filename, 'w', encoding='utf-8') as f_out:
#         for i in range(len(data)):
#             s = ''
#             for value in data[i].values():
#                 s += value + ','
#             f_out.write(f'{s[:-1]}\n')

# def print_result(data:list):
#     print('-'*10)
#     for elem in data:
#         for key in elem:
#             print(f"{key} : {elem[key]}")
#         print('-'*10)

# def get_search_name():
#     return input('Фамилия: ')

# def find_by_name(data:list, name: str):
#     result = []
#     for elem in data:
#         if elem['Фамилия'] == name:
#             result.append(elem)
#     return result

# def find_by_number(data:list, number: str):
#     result = []
#     for elem in data:
#         if elem['Телефон'] == number:
#             result.append(elem)
#     return result

# def get_new_user():
#     fields = ["Фамилия", "Имя", "Телефон", "Описание"]
#     record = dict(zip(fields, input('Введите фамилию, имя, номер, описание').strip().split(',')))
#     return record
    
# def add_user(data:list, user:dict):
#     return data.append(user)

# def write_csv(filename:str, data:list):
#     with open(filename, 'w', encoding='utf-8') as f_out:
#         for i in range(len(data)):
#             s = ''
#             for value in data[i].values():
#                 s += value + ','
#             f_out.write(f'{s[:-1]}\n')

# def delete_by_name(data:list, name: str):
#     for elem in data:
#         if elem['Фамилия'] == name:
#             data.remove(elem)
#     return data

# def work_with_phonebook():
#     choice = show_menu()
#     phone_book = read_csv('seminar_08\phonebook.csv')

#     while(choice!=7):
#         if choice == 1:
#             print_result(phone_book)
#         elif choice == 2:
#             name = get_search_name()
#             print_result(find_by_name(phone_book, name))
#         elif choice == 3:
#             num = input("номер: ")
#             print_result(find_by_number(phone_book, num))
#         elif choice == 4:
#             new_user = get_new_user()
#             add_user(phone_book, new_user)
#             write_csv('seminar_08\phonebook.csv', phone_book)
#         elif choice == 5:
#             del_name = get_search_name()
#             delete_by_name(phone_book, del_name)
#             write_csv('seminar_08\phonebook.csv', phone_book)
#         elif choice == 6:
#             write_txt('phonebook.txt', phone_book)
#         choice = show_menu()
# work_with_phonebook()

# # printing the heading of the program 
# print( "WELCOME TO THE PHONEBOOK DIRECTORY") 


# # creating a .txt file to store contact details 
# filename = "myphonebook.txt" 
# myfile = open(filename, "a+") 
# myfile.close 

# # defining main menu 
# def main_menu(): 
#     print( "\nMAIN MENU\n") 
#     print( "1. показать все контакты") 
#     print( "2. добавить новый контакт") 
#     print( "3.показать существующие контакты") 
#     print( "4. выход") 
#     choice = input("введите свой выбор: ") 
#     if choice == "1": 
#         myfile = open(filename, "r+") 
#         filecontents = myfile.read() 
#         if len(filecontents) == 0: 
#             print( "нету контакта в списке.") 
#         else: 
#             print(filecontents) 
#         myfile.close 
#         enter = input("нажми ентер для продолжения ...") 
#         main_menu() 
#     elif choice == "2": 
#         newcontact() 
#         enter = input("нажми ентер для продолжения ...") 
#         main_menu() 
#     elif choice == "3": 
#         searchcontact() 
#         enter = input("нажми ентер для продолжения ...") 
#         main_menu() 
#     elif choice == "4": 
#         print("Thank you for using Phonebook!") 
#     else: 
#         print( "пожалуйста обеспечте valid input!\n") 
#         enter = input( "нажми ентер для продолжения ...") 
#         main_menu() 
 
# # defining search function         
# def searchcontact(): 
#     searchname = input( "введите имя для поиска контакта в записи: ") 
#     remname = searchname[1:] 
#     firstchar = searchname[0] 
#     searchname = firstchar.upper() + remname 
#     myfile = open(filename, "r+") 
#     filecontents = myfile.readlines() 
      
#     found = False 
#     for line in filecontents: 
#         if searchname in line: 
#             print( "Your Required Contact Record is:", end = " ") 
#             print( line) 
#             found = True 
#             break 
#     if found == False: 
#         print( "The Searched Contact is not available in the Phone Book", searchname) 
 
# # first name 
# def input_firstname(): 
#     first = input( "введите своё имя: ") 
#     remfname = first[1:] 
#     firstchar = first[0] 
#     return firstchar.upper() + remfname 
 
# # last name 
# def input_lastname(): 
#     last = input( "введите свою фамилию: ") 
#     remlname = last[1:] 
#     firstchar = last[0] 
#     return firstchar.upper() + remlname 
 
# # storing the new contact details 
# def newcontact(): 
#     firstname = input_firstname() 
#     lastname = input_lastname() 
#     phoneNum = input( "введите свой номер телефона: ") 
#     emailID = input( "Enter your E-mail Address: ") 
#     contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
#     myfile = open(filename, "a") 
#     myfile.write(contactDetails) 
#     print( "The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!") 
 
# main_menu() 



    