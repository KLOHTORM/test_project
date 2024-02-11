"""
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)

Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""

lst = [0, -1, 5, 2, 3]
counter = 0

for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        counter +=1
print(counter)

res = []    # Получение только нечетных элементов
for el in lst:
    if el % 2 == 1:
        res.append(el)
print(res)

res_02 = []    # Получение только нечетных элементов по индексу
for i in range(0, len(lst), 2):
    if lst[i] % 2 == 1:
        res_02.append(lst[i])
print(res_02)