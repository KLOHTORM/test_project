new_lst = [10, 11, 13, 14]
for elem in new_lst:
    if elem % 2 == 0:
        print(f'{elem} - четное')
    else: print(f'{elem} - нечетное')

print()

for i in range(1, len(new_lst)):    #первый индекс стоящий в скобках в функции range, начинает проверку с данного индекса, а не с начала списка
    if new_lst[i] % 2 == 0:
        print(f'{new_lst[i]} - четное')
    else: print(f'{new_lst[i]} - нечетное')

print()

count = 0
while count < len(new_lst):
    if new_lst[count] % 2 == 0:
        print(f'{new_lst[count]} - четное')
    else: print(f'{new_lst[count]} - нечетное')
    count += 1