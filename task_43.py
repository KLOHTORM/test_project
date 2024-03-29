"""
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.

Ввод:        Вывод:
1 2 3 2 3    2
"""

nums = [1, 2, 3, 2, 3, 3, 3, 3]
my_set = set(nums)
res = []
for el in my_set:
    res.append(nums.count(el) // 2)
print(sum(res))