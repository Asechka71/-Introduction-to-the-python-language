# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

arr = [1,1,2,2,3,4,1,5]
lst = []
for i in range(len(arr)):
    arr2 = arr.copy()
    check = arr2[i]
    arr2.pop(i)
    if check not in arr2:
        lst.append(check)
print(lst)