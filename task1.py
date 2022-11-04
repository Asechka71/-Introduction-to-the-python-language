# Задача: Доделать информационную систему позволяющую работать с сотрудниками некой компании.


dict_data = {'Surname' : [],'Name' : [], 'Discharge' : [], 'Description' : [], 'Salary': [],'ID' : []}

def import_data (file_name):
    data_file = open(file_name, 'r')
    data = data_file.read()

    if '\n\n' in data:
        one_string = data.split('\n\n') # если в файле на одной строке хранится все записи, символ разделитель - ","
        for i in range(len(one_string)):
            dict_data['Surname'].append(one_string[i].split('\n')[0])
            dict_data['Name'].append(one_string[i].split('\n')[1])
            dict_data['Discharge'].append(one_string[i].split('\n')[2])
            dict_data['Salary'].append(10000 + (int(dict_data['Discharge'][-1])*1000))
            dict_data['Description'].append(one_string[i].split('\n')[3])
            dict_data['ID'].append(one_string[i].split('\n')[4])
    else:
        one_string = data.split('\n') # если в файле на одной строке хранится одна часть записи, разделитель - пустая строка
        for i in range(len(one_string)):
            dict_data['Surname'].append(one_string[i].split(',')[0])
            dict_data['Name'].append(one_string[i].split(',')[1])
            dict_data['Discharge'].append(one_string[i].split(',')[2])
            dict_data['Salary'].append(10000 + (int(dict_data['Discharge'][-1])*1000))
            dict_data['Description'].append(one_string[i].split(',')[3])
            dict_data['ID'].append(one_string[i].split(',')[4])

def export_data (file_name):
    new_output = ''
    for i in range(len(dict_data['Surname'])):
        new_output += str(dict_data['Surname'][i] + ',' + dict_data['Name'][i] + ',' + dict_data['Discharge'][i] + ',' + dict_data['Description'][i] + ',' + dict_data['ID'][i])
        new_output += '\n'    
    res = open(file_name,"w")
    res.write(new_output)
    res.close()

print("*** Добро пожаловать в базу данных сотрудников ***\n")
while True:
    print("Пожалуйста, выберите пункт меню:\n\
    1. Импортировать данные из файла\n\
    2. Добавить новую запись в базу\n\
    3. Найти запись в базе\n\
    4. Показать все данные базы\n\
    5. Изменить разряд (повысить/понизить сотрудника)\n\
    6. Удалить запись сотрудника \n\
    7. Экспортировать данные в файл\n\
    8. Закрыть базу данных")
    choice = input("\nВведите номер пункта: ")
    if choice in "1 2 3 4 5 6 7 8":
        choice = int(choice)
        if choice == 1:
            import_data("in.txt")
        elif choice == 2:
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            discharge = input("Введите разряд: ")
            description = input("Введите описание: ")
            id = input("Введите табельный номер: ")

            dict_data['Surname'].append(surname)
            dict_data['Name'].append(name)
            dict_data['Discharge'].append(discharge)
            dict_data['Description'].append(description)
            dict_data['ID'].append(id)

        elif choice == 3:

            while True:
                print("\nВведите аттрибут для поиска:\n    1. Фамилия\n    2. Табельный номер\n    3. Назад")
                search = input("\nВыберите номер пункта: ")
                if search in "1 2 3":
                    search = int(search)
                    if search == 1:
                        attribute_for_search = input("Введите Фамилию: \n")
                        check = '\nЗапись не найдена.\n'
                        for i in range(len(dict_data['Surname'])):
                            if dict_data['Surname'][i] == attribute_for_search:
                                print(f"\n{dict_data['Surname'][i]}, {dict_data['Name'][i]}, {dict_data['Discharge'][i]}, {dict_data['Salary'][i]}, {dict_data['Description'][i]}, {dict_data['ID'][i]}")
                                check = ''
                        print(check)
                    elif search == 2:
                        attribute_for_search = input("Введите табельный номер: ")
                        check = '\nЗапись не найдена.\n'
                        for i in range(len(dict_data['ID'])):
                            if dict_data['ID'][i] == attribute_for_search:
                                print(f"\n{dict_data['Surname'][i]}, {dict_data['Name'][i]}, {dict_data['Discharge'][i]}, {dict_data['Salary'][i]}, {dict_data['Description'][i]}, {dict_data['ID'][i]}")
                                check = ''
                        print(check)
                    elif search == 3:
                        break
                else:
                    print("Данный пункт отсутствует.")
        elif choice == 4:
            print('\nВсе данные базы:\n')
            for i in range(len(dict_data['Surname'])):
                print(f"{dict_data['Surname'][i]}, {dict_data['Name'][i]}, {dict_data['Discharge'][i]}, {dict_data['Salary'][i]}, {dict_data['Description'][i]}, {dict_data['ID'][i]}")
            print('\n')
        elif choice == 5: 
            attribute_for_search = input("Введите табельный номер: ")
            check = '\nЗапись не найдена.\n'
            for i in range(len(dict_data['ID'])):
                if dict_data['ID'][i] == attribute_for_search:
                    change_rate = int(input('Введите новый разряд: '))
                    dict_data['Discharge'][i] = change_rate
                    dict_data['Salary'][i] = 10000 + dict_data['Discharge'][i]*1000 
                    print(f"\n{dict_data['Surname'][i]}, {dict_data['Name'][i]}, {dict_data['Discharge'][i]}, {dict_data['Salary'][i]}, {dict_data['Description'][i]}, {dict_data['ID'][i]}")
                    check = ''
            print(check) 

        elif choice == 6: 
            attribute_for_search = input("Введите табельный номер: ")
            check = '\nЗапись не найдена.\n'
            for i in range(len(dict_data['ID'])):
                if dict_data['ID'][i] == attribute_for_search:
                    dict_data['Surname'].pop(i)
                    dict_data['Name'].pop(i)
                    dict_data['Discharge'].pop(i)
                    dict_data['Salary'].pop(i)
                    dict_data['Description'].pop(i)
                    dict_data['ID'].pop(i)
                    check = 'Запись удалена'
                    break
            print(check) 

        elif choice == 7:
            export_data("out_txt")

        elif choice == 8:
            print("\nСпасибо, что воспользовались нашей базой данных.\n")
            break
    else: 
        print("Введен неверный пункт")
        break