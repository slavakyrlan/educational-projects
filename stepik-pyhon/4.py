'''
Произведение чисел
Напишите программу для определения, является ли число произведением двух чисел из данного набора. Программа должна выводить результат в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число n(0<n<1000) – количество чисел в наборе. В последующих n строках вводятся целые числа, составляющие набор (могут повторяться). Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.

Формат выходных данных
Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.
'''

l = [int(input()) for n in range(int(input()))]
n = int(input())
fl = False

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] * l[j] == n:
            fl = True
            break

print('ДА' if fl == True else 'НЕТ')

''' Error 
n = int(input())
lene = []
for i in range(n):
    num.append(int(input()))
m = int(input())

c = 'НЕТ'
for i in range(len(num)):
    if num[i]*n == m:
        c='ДА'

print(c)'''
''' Error
numbers = []
result = 'НЕТ'
length = int(input())
for i in range(length):
    numbers.append(int(input()))
n = int(input())
for i in range(length):
    for j in range(length):
        if i != j and numbers[i] * numbers[j] == n:
            result = 'ДА'
print(result)'''