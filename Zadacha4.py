# Задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах. Пример:
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:          12W1B12W3B24W1B14W

# сжатие данных
data1 = open('file_with_inDataDeployed.txt', 'r')
count=1
myNewData = []
for line in data1:
    line = list(line)
for index in range(1, len(line)):
        if line[index-1]==line[index] and index != len(line)-1:
            count+=1
        elif line[index-1]!=line[index] and index != len(line)-1:
            myNewData.append(count)
            myNewData.append(line[index-1])
            count=1
        elif index == len(line)-1:
            count += 1
            myNewData.append(count)
            myNewData.append(line[index])
data1.close()
# print(''.join(map(str,myNewData)))
with open('file_with_outDataCompression.txt', 'w') as data2:
    data2.write(''.join(map(str, myNewData)))

# восстановление данных
data3 = open('file_with_inDataCompression.txt', 'r')
myNewData = []
for line in data3:
    line = list(line)
for index in range(1, len(line)):
    if line[index-1].isdigit() and not line[index].isdigit():
        myNewData.append(int(line[index-1])*line[index])
    elif line[index-1].isdigit() and line[index].isdigit():
        line[index]= line[index-1] + line[index]
data3.close()
# print(''.join(map(str,myNewData)))
with open('file_with_outDataDeployed.txt', 'w') as data4:
    data4.write(''.join(map(str, myNewData)))
