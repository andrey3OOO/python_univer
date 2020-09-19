# 01
# errors = 0
# for errors in range(0, 5, 1):
#     errors += int(input("Enter number of errors:"))
# print("Total number of errors:", errors)

# 02
# CALORIES_PER_MINUTE = 4.2
# burned = 0
# for minutes in range(10, 30, 5):
#     print("Burned after", minutes, "min:", minutes*CALORIES_PER_MINUTE)

# 03
# monthly_budget = int(input("Enter your monthly budget: "))
# is_last_category = "n"
# sum_of_categories = 0
#
# while is_last_category == "n":
#     sum_of_categories += int(input("Enter sum for category:  "))
#     is_last_category = input("Is this last category? y/n ")
# print("Total sum: ", sum_of_categories)
# print("Result (left): ", monthly_budget-sum_of_categories)

# 04
# speed = int(input("Speed km/h: "))
# hours = int(input("Hours: "))
# distance = speed*hours
# dist = speed/hours
# total = 0
#
# for i in range(1, hours+1, 1):
#     total += dist
#     print(i, total)
# 05
# years = int(input("Enter number of years: "))
# rainfall_volume = 0
# month_count = 0
#
# for y in range(1, years+1, 1):
#     for m in range(1, 13, 1):
#         print("Enter rainfall size for month", m, ", ", "year ", y, ":")
#         rainfall_volume += int(input())
#         month_count += 1
# print("Total rainfall_volume: ", rainfall_volume)
# print("month_count:", month_count)
# print("average is :", rainfall_volume/month_count)

# 06
# for c in range(0, 21, 1):
#     print(c, "C =", (9/5)*c+32, "F")
# 07
# days = int(input("Enter number of days: "))
# salary_for_day = 1
# salary_total = 0
# for i in range(1, days+1, 1):
#     print("day: ", i)
#     print("salary: ", salary_for_day)
#     salary_for_day *= 2
#     salary_total += salary_for_day
# print("Total salary in rubles: ", salary_total/100)
# 08
# n = 0
# sum_n = 0
# while n >= 0:
#     n = int(input("Enter number: "))
#     if n < 0:
#         break
#     sum_n += n
# print("Sum is ", sum_n)

# 09
# ocean_level = 0
# for year in range(1, 26, 1):
#     ocean_level += 1.6
#     print("Year: ", year, ", ocean level: ", round(ocean_level, 2), "mm")
#
# 10
TUITION_PRICE_SEMESTER = 45000
INCREASE_YEARS = 5
tuition_price_year = TUITION_PRICE_SEMESTER*2

for year in range(1, INCREASE_YEARS+1, 1):
    tuition_price_year = tuition_price_year+tuition_price_year*0.03
    print("Year", year, ", Increased price for semester:", round(tuition_price_year/2, 2))
