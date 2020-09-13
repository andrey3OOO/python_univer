# 01
# x = 101
# y = 2
# z = 3
# if x > 100:
#     y = 20
#     z = 40
# print(x)
# print(y)
# print(z)

# 02
# a = 9
# b = 2
# c = 3
# if a < 10:
#     b = 0
#     c = 1
# print(a)
# print(b)
# print(c)

# 03
# a = 11
# b = 1
# if a < 10:
#     b = 0
# else:
#     b = 99
# print(a)
# print(b)

# 04
# score = 1
# A_score = 2
# B_score = 3
# C_score = 4
# D_score = 5
# if score >= A_score:
#     print('Ваш уровень - А.')
# else:
#     if score >= B_score:
#         print('Ваш уровень - В. ')
#     else:
#         if score >= C_score:
#             print('Ваш уровень - С. ')
#         else:
#             if score >= D_score:
#                 print('Baш уровень - D.')
#             else:
#                 print('Ваш уровень - F. ')
# 05
# amount1 = 11
# amount2 = 15
# if amount1 > 10 and amount2 < 100:
#     if amount1 > amount2:
#         print(amount1)
#     else:
#         print(amount2)
# 06
# SPEED = 40
# if SPEED >= 24 and SPEED <= 56:  # if 24 <= SPEED <= 56:
#     print("Speed is OK")
# else:
#     print("Speed is NOT OK")

# 07
# points = 9
# if points < 9 or points > 51:
#     print("Invalid points")
# else:
#     print("Valid points")

# 08
# import turtle
#
# if turtle.heading() >= 0 and turtle.heading() <= 45:
#     turtle.penup()
# turtle.done()

# 09
# import turtle
# if turtle.pencolor() == 'blue' or turtle.pencolor() == 'red':
#     turtle.pensize(5)  # pensize() = 5?
# turtle.done()

# 10
# import turtle
# SCREEN_WIDTH = 600  # Ширина экрана.
# SCREEN_HEIGHT = 600  # Высота экрана.
# TARGET_LLEFT_Х = 100  # Левая нижняя координата х цели.
# TARGET_LLEFT_У = 200  # Левая нижняя координата у цели.
# TARGET_WIDTH = 100  # Ширина цели.
# NORTH = 90  # Угол северного направления.
# SOUTH = 270  # Угол южного направления.
# EAST = 0  # Угол восточного направления.
# WEST = 180  # Угол западного направления.
# #Настроить окно.
# # turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
# # Нарисовать цель.
# turtle.hideturtle()
# turtle.speed(0)
# turtle.penup()
# turtle.goto(TARGET_LLEFT_Х, TARGET_LLEFT_У)
# turtle.pendown()
# turtle.setheading(EAST)
# turtle.forward(TARGET_WIDTH)
# turtle.setheading(NORTH)
# turtle.forward(TARGET_WIDTH)
# turtle.setheading(WEST)
# turtle.forward(TARGET_WIDTH)
# turtle.setheading(SOUTH)
# turtle.forward(TARGET_WIDTH)
# turtle.penup()
#
# turtle.done()