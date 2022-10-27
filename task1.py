# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

a=[randint(1,10) for i in range(5)]
print(a)

# Первоначальный вид программы:
# sum = 0
# for i in range(len(a)):
#     if i % 2 == 0:
#         sum += a[i]

list =[a[i] for i in range(len(a)) if i % 2 == 0]
print(sum(list)) 