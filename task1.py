# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# - под форматами понимаем структуру файлов, например: 
# в файле на одной строке хранится одна часть записи, разделитель - пустая строка


dict_data = {'Surname' : [],'Name' : [], 'Phone' : [], 'Description' : []}

def import_data (file_name):
    data_file = open(file_name, 'r')
    data = data_file.read()

    if '\n\n' in data:
        one_string = data.split('\n\n') # если в файле на одной строке хранится все записи, символ разделитель - ","
        for i in range(len(one_string)):
            dict_data['Surname'].append(one_string[i].split('\n')[0])
            dict_data['Name'].append(one_string[i].split('\n')[1])
            dict_data['Phone'].append(one_string[i].split('\n')[2])
            dict_data['Description'].append(one_string[i].split('\n')[3])
    else:
        one_string = data.split('\n') # если в файле на одной строке хранится одна часть записи, разделитель - пустая строка
        for i in range(len(one_string)):
            dict_data['Surname'].append(one_string[i].split(',')[0])
            dict_data['Name'].append(one_string[i].split(',')[1])
            dict_data['Phone'].append(one_string[i].split(',')[2])
            dict_data['Description'].append(one_string[i].split(',')[3])
def export_data (file_name):
    new_output = ''
    for i in range(len(dict_data['Surname'])):
        new_output += str(dict_data['Surname'][i] + ',' + dict_data['Name'][i] + ',' + dict_data['Phone'][i] + ',' + dict_data['Description'][i])
        new_output += '\n'
    
    res = open(file_name,"w")
    res.write(new_output)
    res.close()

print("*** Добро пожаловать в справочник ***\n")
while True:
    print("Пожалуйста, выберите пункт меню:\n\
    1. Импортировать данные из файла\n\
    2. Добавить новую запись в справочник\n\
    3. Найти запись в справочнике\n\
    4. Показать данные из справочника\n\
    5. Экспортировать данные в файл\n\
    6. Закрыть справочник")
    choice = input("\nВведите номер пункта: ")
    if choice in "1 2 3 4 5 6":
        choice = int(choice)

        if choice == 1:
            import_data("in.txt")

        elif choice == 2:
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            description = input("Введите описание: ")

            dict_data['Surname'].append(surname)
            dict_data['Name'].append(name)
            dict_data['Phone'].append(phone)
            dict_data['Description'].append(description)

        elif choice == 3:

            while True:
                print("\nВведите аттрибут для поиска:\n    1. Фамилия\n    2. Телефон\n    3. Назад")
                search = input("\nВыберите номер пункта: ")
                if search in "1 2 3":
                    search = int(search)
                    if search == 1:
                        attribute_for_search = input("Введите Фамилию: \n")
                        check = '\nЗапись не найдена.\n'
                        for i in range(len(dict_data['Surname'])):
                            if dict_data['Surname'][i] == attribute_for_search:
                                print(f"\n{dict_data['Surname'][i]}, {dict_data['Name'][i]}, {dict_data['Phone'][i]}, {dict_data['Description'][i]}")
                                check = ''
                        print(check)
                    elif search == 2:
                        attribute_for_search = input("Введите Телефон: ")
                        check = '\nЗапись не найдена.\n'
                        for i in range(len(dict_data['Surname'])):
                            if dict_data['Phone'][i] == attribute_for_search:
                                print(f"\n{dict_data['Surname'][i]}, {dict_data['Name'][i]}, {dict_data['Phone'][i]}, {dict_data['Description'][i]}")
                                check = ''
                        print(check)
                    elif search == 3:
                        break
                else:
                    print("Данный пункт отсутствует.")


        elif choice == 4:
            print('\nДанные справочника:\n')
            for i in range(len(dict_data['Surname'])):
                print(f"{dict_data['Surname'][i]}, {dict_data['Name'][i]}, {dict_data['Phone'][i]}, {dict_data['Description'][i]}")
            print('\n')

        elif choice == 5:
            export_data("out_txt")

        elif choice == 6:
            print("\nСпасибо, что воспользовались нашим справочником.\n")
            break

    else: 
        print("Введен неверный пункт")
        break


# Задание было выполнено в одиночку.