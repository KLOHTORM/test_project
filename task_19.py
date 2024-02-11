"""
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K индексов элементов вправо, K –
положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

lst = [1, 2, 3, 4, 5]
k = 3

new_lst = lst[k:] + lst[:k]
print(new_lst )

for i in range(k - 1):   # другое решение
    last_i = lst.pop()
    lst.insert(0, last_i)
print(lst)