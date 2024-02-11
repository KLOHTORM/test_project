"""
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива

Ввод:               Вывод:
7                   3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1      (каждое число вводится с новой строки)

"""

lst_1 = [3, 1 , 3 , 4 , 2 , 4, 12]
lst_2 = [4, 15, 43, 1, 15, 1]
lst_res = []
# 1 способ
for el in lst_1:
    if el not in lst_2:
        lst_res.append((el))
print(lst_res)

# 2 способ
lst_res = [el for el in lst_1 if el not in lst_2]
print(lst_res)

