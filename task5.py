# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


f = open('one.txt', 'r')
a = f.read()
f.close()
a = a.replace(' ','')
a = a.replace('=0','')
a = a.split('+')

f2 = open('two.txt', 'r')
b = f2.read()
f2.close()
b = b.replace(' ','')
b = b.replace('=0','')
b = b.split('+')

a = [i.strip() for i in a]
b = [i.strip() for i in b]

dict_a = dict()
dict_b = dict()

for i in a:
    if i[-1] == 'x':
        if i[-1] not in dict_a.keys():
            dict_a[i[-1]] = int(i[:-1])
        else:
            dict_a[i[-1]] += int(i[:-1])
    elif 'x' not in i:
        if '0' not in dict_a.keys():
            dict_a['0'] = int(i)
        else:
            dict_a['0'] += int(i)
    else:
        if i[-3:] not in dict_a.keys():
            dict_a[i[-3:]] = int(i[:-3])
        else:
            dict_a[i[-3:]] += int(i[:-3])

for i in b:
    if i[-1] == 'x':
        dict_b[i[-1]] = int(i[:-1])
    elif 'x'not in i:
        dict_b['0'] = int(i)
    else:
        dict_b[i[-3:]] = int(i[:-3])

dict_sum = dict()

for key, value in dict_a.items():
    dict_sum[key] = 0

for key, value in dict_b.items():
    dict_sum[key] = 0

for key, value in dict_sum.items():
    try:
        dict_sum[key] += dict_a[key]
    except:
        pass
    try:
        dict_sum[key] += dict_b[key]
    except:
        pass

sorted_dict = dict(sorted(dict_sum.items(),reverse=True))

final_string = ''

for key, value in sorted_dict.items():
    if key != '0':
        final_string +=  str(value) + key
        final_string += ' + '
    else:
        final_string += str(value)

final_string += ' = 0'

f3 = open('three.txt','w')  
f3.write(final_string) 
f3.close() 