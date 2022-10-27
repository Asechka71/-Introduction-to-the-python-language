# Реализуйте алгоритм перемешивания списка.

from random import randint
import random

print('Введите размер списка:')
n=int(input())
a=[randint(-10,10) for i in range(n)]

# Первоначальный код:
# print(a, '\n')
# random.shuffle(a)
# print(a)

b = sorted(a, key=lambda x: random.random())
print(a)
print(b)