"""
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).

Input: 2 -> 3 4
Output: 4 3
"""

str = '3 4'

def func_1(n):
    res = ''
    for el in reversed(n):
        res += el
    return res
print(func_1(str))

def func_2(n):
    if len(n) == 1:
        return n
    return n[-1] + func_2(n[:-1])
print(func_2(str))