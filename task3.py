# Реализуйте RLE алгоритм: реализуйте модуль сжатия и 
# восстановления данных. Входные и выходные данные хранятся
# в отдельных текстовых файлах.


array = open("in.txt","r")
input_data = array.read()
array.close()

current_value = input_data[0]
counter = 1
output_data = str()
for i in range(1, len(input_data)):
    if input_data[i] == current_value:
        counter +=1
    else:
        output_data += str(counter) + current_value
        current_value = input_data[i]
        counter = 1
output_data += str(counter) + current_value

res = open("out.txt", "w")
res.write(output_data)
res.close()

print(output_data)

array1 = open("out.txt","r")
input_data2 = array1.read()
array1.close()

new_output = ''

for i in range(0, len(input_data2), 2):
    new_output += input_data2[i+1] * int(input_data2[i])

res2 = open("out2.txt","w")
res2.write(new_output)
res2.close()

print(new_output)