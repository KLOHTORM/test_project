"""
Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза

Input: 5 -> 5 1 6 5 9
Output: 1 9
"""
from typing import List

#w_mell = [5, 1, 6, 5, 9]
w_mell = list(map(int, input("Введите числа через пробел: ").split()))

print(f'Для себя: {max(w_mell)}, для тещи: {min(w_mell)}')