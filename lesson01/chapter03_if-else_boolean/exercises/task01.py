# 01
# number = int(input("Enter the number: "))
# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuesday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number == 5:
#     print("Friday")
# elif number == 6:
#     print("Saturday")
# elif number == 7:
#     print("Sunday")
# else:
#     print("Error number")

# 02
# length_1 = int(input("Enter length of first rectangle: "))
# width_1 = int(input("Enter the width of first rectangle: "))
# length_2 = int(input("Enter length of second rectangle: "))
# width_2 = int(input("Enter the width of second rectangle: "))
#
# area_1 = length_1*width_1
# area_2 = length_2*width_2
#
# if area_1 > area_2:
#     print("area 1 more than area 2")
# elif area_1 < area_2:
#     print("area 2 more than area 1")
# else:
#     print("areas are same")

# 03
# age = float(input("Enter the age: "))
# if age <= 1:
#     print("Baby")
# elif 1 < age < 13:
#     print("Child")
# elif 13 < age < 20:
#     print("Teenager")
# elif age < 20:
#     print("Adult")

# 04
# number = int(input("Enter the number: "))
# if number == 1:
#     print("I")
# elif number == 2:
#     print("II")
# elif number == 3:
#     print("III")
# elif number == 4:
#     print("IV")
# elif number == 5:
#     print("V")
# elif number == 6:
#     print("VI")
# elif number == 7:
#     print("VII")
# elif number == 8:
#     print("VIII")
# elif number == 9:
#     print("IX")
# elif number == 10:
#     print("X")
# else:
#     print("Error number")

# 05
# mass = int(input("Enter the mass: "))
#
# if mass > 500:
#     print("Too heavy")
# elif mass < 100:
#     print("Too light")
# else:
#     print("Weight is ", mass * 9.8, " kg")

# 06
# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))
# if day*month == year:
#     print("Magic")
# else:
#     print("There is no magic")
#
# 07
# color_mixer_1 = input("Enter first color: ")
# color_mixer_2 = input("Enter second color: ")
#
# if color_mixer_1 == "red" and color_mixer_2 == "blue":
#     print("Violet")
# elif color_mixer_1 == "red" and color_mixer_2 == "yellow":
#     print("Orange")
# elif color_mixer_1 == "blue" and color_mixer_2 == "yellow":
#     print("Green")
# else:
#     print("Error")

# 08
# number_of_people = int(input("Enter number_of_people: "))
# number_of_hotdogs_for_each = int(input("Enter number_of_hotdogs: "))
#
# number_of_hotdogs_total = number_of_hotdogs_for_each*number_of_people
# number_of_hotdog_packages = int(number_of_hotdogs_total/10)
# number_of_hotbuns_packages = int(number_of_hotdogs_total/8)
# number_of_hotdog_packages_rest = number_of_hotdogs_total % 10
# number_of_hotbuns_packages_rest = number_of_hotdogs_total % 8
#
# print("number_of_hotdogs_total: ", number_of_hotdogs_total)
# print("number_of_hotdog_packages", number_of_hotdog_packages)
# print("number_of_hotbuns_packages", number_of_hotbuns_packages)
# print("number_of_hotdog_packages_rest", number_of_hotdog_packages_rest)
# print("number_of_hotbuns_packages_rest", number_of_hotbuns_packages_rest)

# 09
# pocket_number = int(input("Enter pocket number: "))
#
# if pocket_number == 0:
#     print("Green")
# elif 1 < pocket_number <= 10:
#     print("Black")
# elif 11 <= pocket_number <= 18:
#     print("Red")
# elif 19 <= pocket_number <= 28:
#     print("Black")
# elif 29 <= pocket_number <= 36:
#     print("Red")
# else:
#     print("Error")

# 10
# number_of_coins_5 = int(input("Enter number_of_coins 5 kopeek: "))
# number_of_coins_10 = int(input("Enter number_of_coins 10 kopeek: "))
# number_of_coins_50 = int(input("Enter number_of_coins 50 kopeek: "))
#
# sum_of_coins = (number_of_coins_5*5)+(number_of_coins_10*10)+(number_of_coins_50*50)
# print(sum_of_coins)
#
# if sum_of_coins < 100:
#     print("Amount is less than 1 ruble")
# elif sum_of_coins > 100:
#     print("Amount is more than 1 ruble")
# elif sum_of_coins == 100:
#     print("You win!")

# 11
# number_of_books = int(input("Enter number of books: "))
# if number_of_books == 0:
#     print("Earned 0 points")
# elif number_of_books == 2:
#     print("Earned", 5, "points")
# elif number_of_books == 4:
#     print("Earned", 15, "points")
# elif number_of_books == 6:
#     print("Earned", 30, "points")
# elif number_of_books >= 8:
#     print("Earned", 60, "points")
# else:
#     print("Bye")

# 12
# number_of_packages = int(input("Enter number of packages: "))
# PRICE = 99
# if 10 <= number_of_packages <= 19:
#     print("Discount is", (PRICE*number_of_packages)*0.1, ", total amount is", (PRICE*number_of_packages)-(PRICE*number_of_packages)*0.1)
# elif 20 <= number_of_packages <= 49:
#     print("Discount is", (PRICE*number_of_packages)*0.2, ", total amount is", (PRICE*number_of_packages)-(PRICE*number_of_packages)*0.2)
# elif 50 <= number_of_packages <= 49:
#     print("Discount is", (PRICE*number_of_packages)*0.3, ", total amount is", (PRICE*number_of_packages)-(PRICE*number_of_packages)*0.3)
# elif number_of_packages >= 100:
#     print("Discount is", (PRICE*number_of_packages)*0.4, ", total amount is", (PRICE*number_of_packages)-(PRICE*number_of_packages)*0.4)
# else:
#     print("Bye")

# 13
# weight = float(input("Enter weight: "))
# weight_index = int(weight/100)
# print(weight_index)
#
# if weight < 200:
#     print("Shipping charged is 150")
# elif weight == 200:
#     print("Shipping charged is 300")
# elif 200 < weight <= 600:
#     print("Shipping charged is", weight_index*300)
# elif 600 < weight <= 1000:
#     print("Shipping charged is", weight_index*400)
# elif weight > 1000:
#     print("Shipping charged is", weight_index*475)
# else:
#     print("Bye")

# 14 problem in book
# weight = float(input("Enter weight: "))
# height = float(input("Enter height: "))
# bmi = weight / (height**2)
#
# if 18.5 <= bmi < 25:
#     print("Your BMI is OK")
# elif bmi < 18.5:
#     print("You underweight")
# elif bmi > 25:
#     print("You overweight")

# 15 not completed
# seconds = int(input("Enter number of seconds: "))
# minutes = int(seconds/60)
# print("minutes", minutes)
# rest_of_seconds_min = seconds % 60
# print("rest_of_seconds_min", rest_of_seconds_min)
#
# hours = int(seconds/3600)
# print("hours", hours)
# rest_of_min_hour = seconds % 3600
# print("rest_of_min_hour", rest_of_min_hour)
#
# days = int(seconds/86400)
# print("days", days)
# rest_of_hour_day = seconds % 86400
# print("rest_of_hour_day", rest_of_hour_day)
#
#
# if 60 < seconds < 3600:
#     print(minutes, "m", rest_of_seconds_min, "s")
# elif 3600 <= seconds < 86400:
#     print(hours, "h", rest_of_min_hour, "m", rest_of_seconds_min, "s")
# elif seconds >= 86400:
#     print(days, "d", rest_of_hour_day, "h", rest_of_min_hour, "m", rest_of_seconds_min, "s")

# 16
# year = int(input("Enter the year: "))
# rest_of_year_100 = year % 100
# rest_of_year_400 = year % 400
# rest_of_year_4 = year % 4
#
# if rest_of_year_100 == 0 and rest_of_year_400 == 0:
#     print(year, "'s February has 29 days")
# elif rest_of_year_100 != 0 and rest_of_year_4 == 0:
#     print(year, "'s February has 29 days")
# else:
#     print(year, "'s February has 28 days")

# 17
answer = input("Reboot PC and try to connect, Did that fix problem? ")
if answer == 'yes':
    print('OK')
elif answer == 'no':
    answer = input("Reboot router and try to connect, Did that fix problem? ")
    if answer == 'yes':
        print('OK')
    elif answer == 'no':
        print('wtow')
