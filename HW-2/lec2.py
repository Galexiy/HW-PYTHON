# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# n = int(input('Введите целое число '))
# print(n)
# sum = 0
# while n > 0:
#     sum = sum + n%10
#     n = n//10    
# print(sum)


# n = input('Введите число ')
# sum = 0
# for i in n:
#     if i != '.':
#         sum += int(i)
# print(sum)

# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму 
# элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


# n = int(input('Введите число '))
# my_list = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# sum = round(sum(my_list), 2)
# print(my_list)
# print(sum)


# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум 
# использование библиотеки Random для получения случайного int

# import random
# my_list = []
# for i in range(10):
#     my_list.append(random.randint(1,100))
# print(my_list)
  
