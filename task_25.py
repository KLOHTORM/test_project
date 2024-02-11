"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""

lst = input("Введите символы через пробел: ").split()   # split - разбивает список на элементы
my_dict = {}

for el in lst:
    if el not in my_dict:
        print(el, end=" ")
    else: print(f"{el}_{my_dict[el]}", end=" ")
    my_dict[el] = my_dict.get(el, 0) + 1