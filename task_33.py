"""
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

lst = input("Введите 5 чисел от 1 до 5 через пробел: ").split()
max_n = max(lst)
min_n = min(lst)
new_lst = []

# for el in lst:
#     if el == max_n:
#         new_lst.append(min_n)
#     else: new_lst.append(el)
# print(new_lst)

def func(lst, new_lst=[], max_n=max(lst), min_n=min(lst)):
    if len(lst) == 0:
        return new_lst
    if lst[0] == max_n:
        new_lst.append(min_n)
    else: new_lst.append(lst[0])
    return func(lst[1:])
print(func(lst))

