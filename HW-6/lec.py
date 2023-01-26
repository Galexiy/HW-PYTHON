# Домашняя работа №6

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Старое решение
# my_list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         sum += my_list[i]
# print(sum)

# Новое решение
# my_list = [2, 3, 5, 9, 3]
# def sum_ind(my_list):
#     return sum(my_list[i] for i in range(1,len(my_list),2))
# sum = sum_ind(my_list)
# print(sum) 

 

# НАПИШИТЕ ПРОГРАММУ КОТОРАЯ НА ВХОД ПРИНИМАЕТ 5 ЧИСЕЛ И ИЗ НИХ ВЫЯВЛЯЕТ МАКСИМАЛЬНОЕ ЧИСЛО 

# мое старое решение 

# a = int(input('Введите  а:  '))
# b = int(input('Введите  b:  '))
# c = int(input('Введите  а:  '))
# d = int(input('Введите  b:  '))
# e = int(input('Введите  а:  '))

# if a > b and a > c and a > d and a > e:  # мой вариант
#     print (a)
# if b > a and b > c and b > d and b > e:
#     print(b)

# max = a
# if b > max: 
#     max = b
# if c > max:
#     max = c
# if d > max:
#     max = d
# if e > max:
#     max = e
# print(max)

# list = [a, b, c, d, e]
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)


# новое решение 

# def max_num(numbers):
#     return max(numbers)

# numbers = [int(x) for x in input('Введите числа через пробел: ').split()]
# result = max_num(numbers)
# print(f'Максимальное число: {result}')



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# Старое решение

# my_list = [2, 3, 5, 6]
# res = []
# count = 0
# for i in range(len(my_list)):
#     if count % 2 == 0:
#         res.append(my_list[i] * my_list[-i-1]) 
# print(res)


# Новое решение

# # my_list = list(map(int, input('Введите числа через пробел:  ').split()))

# my_list = [int(x) for x in input('Введите числа через пробел: ').split()]
# new_list = []
# for i in range(0, len(my_list)//2):
#     new_list.append(my_list[i] * my_list[len(my_list)-1-i])
# if len(my_list) % 2 != 0:
#     new_list.append(my_list[len(my_list)//2] ** 2)
# print(new_list)

