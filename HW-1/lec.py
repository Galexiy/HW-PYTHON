# Домашняя работа №1

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input('Введите число дня недели:  '))
# print(a)

# if a == 6 or a == 7:
#     print('Сегодня - выходной')
# else:
#     print('Сегодня рабочий день недели')

# if a > 7 or a < 0:
#     print('Значение введено не правильно')



# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# x = int(input('Введите координату точки X:  '))
# print(x)
# y = int(input('Введите координату точки Y:  '))
# print(y)

# if x == 0 and y == 0:
#     print('Точка расположена в нулевых координатах')

# if x > 0 and y > 0:
#     print ('Точка расположена в первой четверти')
# if x < 0 and y > 0:
#     print ('Точка расположена во второй четверти ')
# if x < 0 and y < 0:
#     print ('Точка расположена в третьей четверти ')
# if x > 0 and y < 0:
#     print ('Точка расположена в четвертой четверти ')


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input('Введите номер четверти:  '))
# print(a)

# if a == 1:
#     print('Координата по оси Х и Y будет положительной ')
# if a == 2:
#     print('Координата по оси Х будет положительной и координата по оси Y будет отрицательной ')
# if a == 3:
#     print('Координата по оси Х и Y  будет отрицательной ')
# if a == 4:
#     print('Координата по оси Х будет положительной и координата по оси Y будет отрицательной ')
# else:
#     print('Значение введены не правильно ')


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# ax = int(input('Введите для точки А координату по оси Х:  '))
# print(ax)
# ay = int(input('Введите для точки А координату по оси Y:  '))
# print(ay)
# bx = int(input('Введите для точки B координату по оси Х:  '))
# print(bx)
# by = int(input('Введите для точки B координату по оси Y:  '))
# print(by)

# import math
# ab = round(math.sqrt(((bx - ax)**2)+((by - ay)**2)),2)

# print("Расстояние между 2-мя точками А и В будет равно")
# print(ab)
