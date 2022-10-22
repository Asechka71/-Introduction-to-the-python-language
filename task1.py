# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# - под форматами понимаем структуру файлов, например: 
# в файле на одной строке хранится одна часть записи, разделитель - пустая строка


data_file = open('in.txt', 'r')
data = data_file.read()
dict_data = {'Surname' : [],'Name' : [], 'Phone' : [], 'Description' : []}

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

new_output = ''
for i in range(len(dict_data['Surname'])):
    print(dict_data['Surname'][i])
    print(dict_data['Name'][i])
    print(dict_data['Phone'][i])
    print(dict_data['Description'][i])
    new_output += str(dict_data['Surname'][i] + ',' + dict_data['Name'][i] + ',' + dict_data['Phone'][i] + ',' + dict_data['Description'][i])
    new_output += '\n'
    print('\n')
    
res = open("out.txt","w")
res.write(new_output)
res.close()

print(new_output)

# Задание было выполнено в одиночку.