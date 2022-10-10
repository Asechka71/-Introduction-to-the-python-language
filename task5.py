# Реализуйте алгоритм перемешивания списка.

from random import randint
import random

print('Введите размер списка:')
n=int(input())
a=[randint(-10,10) for i in range(n)]
print(a, '\n')
random.shuffle(a)
print(a)