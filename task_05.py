"""
Вагоны в электричке пронумерованны натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от "головы"
поезда, а иногда - с "хвоста"; Это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
Витя сел в 1 вагон от головы поезда и обнаружил, что его вагон имеет номер 1. Он хочет определить, сколько всего вагонов
в электричке. Напишите программу, которая будет это делать или сообщать, что без доп. информации это сделать невозможно.

Input: 3 4 (ввод на разных строках)
Output: 6
"""

i, j = 3, 4

if i != j:
    print(i + j - 1)
else: print ("задача нерешаема")