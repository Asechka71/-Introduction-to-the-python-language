# Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле 
# file.txt в одной строке одно число.

from random import randint

print('Введите размер списка N:')
n=int(input())
a=[randint(-n,n) for i in range(n)]
print(a)

b = []
path = 'text.txt'
data = open(path, 'r')
data_exp = data.read()
data.close()

indexies = data_exp.split('\n')

multiply = 1
for i in indexies:
    multiply = multiply * a[int(i)]

print(multiply)