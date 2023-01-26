# ДЗ 4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

k = int (input ('Введите натуральную степень k: '))
equation = {}
for i in range(k, -1, -1):
    equation[i] = random.randint(0, 100)
# print(equation)

eq_str = ' '
for k,v in equation.items():
    if k == 1:
        eq_str += f'{v}*x + '
    elif k == 0:
        eq_str += f'{v} + '
    elif v == 1:
        eq_str += f' '
    else:
        eq_str += f' {v}*x**{k} + '
else:
    eq_str = eq_str[:-3] + ' = 0'
print(eq_str)


