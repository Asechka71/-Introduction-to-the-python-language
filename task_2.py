# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a = [2,3,4,5,6]
print(a)
a1 =[]
if len(a)%2 != 0: b = len(a)//2 +1
if len(a)%2 == 0: b = len(a)//2 

for i in range(len(a)):
        x = (a[i])*(a[-(i+1)])
        a1.append(x) 
        len(a1)

print(a1[:b])       