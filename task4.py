# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint

print("Введите натуральную степень к:")
k = int(input())
res = ''
while k != 0:
    c = randint(0,100)
    if c != 0:
        if k != 1:
            res += f'{c}*xˆ{k} + '
        else: 
            res += f'{c}*x + '
    k = k -1
res += f'{randint(0,100)} = 0'
file = open("otus.txt", "w")
file.write(res)
file.close()