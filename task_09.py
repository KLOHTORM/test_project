"""
По данному целому неотрицательному n вычислите значение n!.
n! = 1 * 2 * 3 * ... * n (произведение всех чисел от 1 до n) 0! = 1
Решить задачу используя цикл while

Input: 5
Output: 120
"""

f = 1
n = 5

while n > 1:
    f *= n
    n -= 1

print(f)