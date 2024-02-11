"""
Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

lst = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(lst)))

lst_dif = []     # другое решение
for i in lst:
    if i not in lst_dif:
        lst_dif.append(i)
print(len(lst_dif))

lst_dif_new = []       # другое решение
for i in range(len(lst)):   # range(число) - цикл выполнится "число" раз
    if lst[i] not in lst_dif_new:
         lst_dif_new.append((lst[i]))
print(len(lst_dif_new))