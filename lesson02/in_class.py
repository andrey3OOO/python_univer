# 1. При помощи цикла for вывести на экран нечетные числа
# от 1 до 99.

def print_even_by_range(start,stop):

# i = 1
# while i < 99:
#     i += 2
#     print(i)

# for i in range(1, 100):
#     if i % 2 !=0:
#         print(i)
#
# recommended
    for i in range(start,stop,2):
        print(i)
# test comment 111111232313 111testd
print_even_by_range(1,100)
# 2. Даны целые числа K и N (N > 0). Вывести N раз число K.

# k = 10
# n = 5
# i = 0
#
# while i < n:
#     i += 1
#     print(k)


# 3. Даны два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B),
# а также количество N этих чисел.


# a = 11
# b = 20
#
# n = 0
#
# if a % 2 == 1:
#     i = a+1
# else:
#     i = a
#
# while i <= b:
#     print(i)
#     i += 2
#     n += 1
# print('\n', n)


# 4. Вывести 10 первых чисел последовательности 0, -5,-10,-15..

# n = 0
# i = 0
# NUMBERS_COUNT = 10
#
# while i < NUMBERS_COUNT:
#     print(n)
#     n -= 5
#     i += 1


# 5. Дано число n при помощи цикла for посчитать n!( n!=n*(n-1)!)
# 5 * 4 * 3 * 2 * 1



# 6. Даны переменные x и n вычислить x^n.

# x = 2
# n = 3
# i = 0
#
# s = 2
#
# while i < n:
#     x *= s
#     i += 1
#     print(x)

# 7. Перепишите программы 5,6 с использованием цикла while.
# 8. Используя циклы и метод:
# print("*"), print(" "), print("\n") (для перехода на новую строку).
# Выведите на экран:
# · прямоугольник
# · прямоугольный треугольник
# · равносторонний треугольник
# · ромб
