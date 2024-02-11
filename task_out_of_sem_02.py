def func_1(n):
    my_sum = 0
    for num in range(n):
        my_sum += num
    return my_sum
print(func_1(10))

def func_2(n, my_sum=0, num=0):
    if num == n:
        return my_sum
    return  func_2(n, my_sum+num, num+1)
print(func_2(10))


