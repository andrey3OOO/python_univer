# 2
# plan = int(input("Enter plan: "))
# print("Profit = ", format(plan*0.23))

# 3
# sqmeters_count = int(input("Enter sqmeters: "))
# print("Akrs = ", sqmeters_count/4047)

# 4
# product_1 = int(input("Enter price for product 1: "))
# product_2 = int(input("Enter price for product 2: "))
# product_3 = int(input("Enter price for product 3: "))
# product_4 = int(input("Enter price for product 4: "))
# product_5 = int(input("Enter price for product 5: "))
# prod_sum = product_1+product_2+product_3+product_4+product_5
#
# print("Sum = ", prod_sum)
# print("Tax = ", prod_sum*0.07)
# print("Total = ", prod_sum+(prod_sum*0.07))

# 5
# SPEED = 70 # constant
# print("Distance for 6h = ", SPEED * 6)
# print("Distance for 10h = ", SPEED * 10)
# print("Distance for 15h = ", SPEED * 15)

# 6
# purchase_sum = int(input("Enter purchase sum: "))
# fed_tax = purchase_sum * 0.05
# reg_tax = purchase_sum * 0.025
# print("Federal tax = ", fed_tax)
# print("Regional tax = ", reg_tax)
# print("Total tax = ", fed_tax+reg_tax)
# print("Total = ", purchase_sum+fed_tax+reg_tax)

# 7
# distance = int(input("Enter distance: "))
# used_gas = int(input("Enter used gas: "))
# print("index: ", distance/used_gas)

# 8
# charge = int(input("Enter food charge: "))
# tax = charge*0.018
# tip = charge*0.07
# total = charge+tax+tip
# print("Total is ", format(total, '.2f'))

# 9
# temperature_c = float(input("Enter C temperature: "))
# temperature_f = ((9/5)*temperature_c)+32
# print("temperature f: ", format(temperature_f, '.2f'))

# 10
# sugar_for_one_cookie = 1.5/48
# butter_for_one_cookie = 1/48
# flour_for_one_cookie = 2.75/48
#
# cookies_count = int(input("Enter cookies count you want: "))
# print("You need sugar: ", format(sugar_for_one_cookie*cookies_count, '.2f'))
# print("butter: ", format(butter_for_one_cookie*cookies_count, '.2f'))
# print("flour: ", format(flour_for_one_cookie*cookies_count, '.2f'))

# 11
# male_count = int(input("Enter male count: "))
# female_count = int(input("Enter female count: "))
# male_index = male_count/(male_count+female_count)
# female_index = female_count/(male_count+female_count)
# print("Male index is: ", format(male_index, '.1f'))
# print("Female index is: ", format(female_index, '.1f'))

# 12
# PURCHASED_STOCKS = 2000
# PURCHASED_PRICE = 40
# TAX = 0.03
# SOLD_STOCKS = 2000
# SOLD_PRICE = 42.75
#
# purchase_sum = PURCHASED_STOCKS*PURCHASED_PRICE
# purchase_tax = purchase_sum*TAX
# purchase_total = purchase_sum + purchase_tax
# sold_sum = SOLD_STOCKS*SOLD_PRICE
# sold_tax = sold_sum*TAX
# sold_total = sold_sum + sold_tax
#
#
# print("Purchase total is ", purchase_total)
# print("Purchase tax is ", purchase_tax)
#
# print("Sold total is ", sold_total)
# print("Sold tax is ", sold_tax)
#
# print("Profit is ", sold_total-purchase_total)

# 13 ? to check
# length = int(input("Enter length: "))
# space_by_endpost = int(input("Enter space_by_endpost: "))
# space_between_vines = int(input("Enter space_between_vines: "))
#
# grapevines_number = (length-(2*space_by_endpost))/space_between_vines
# print("grapevines number is ", grapevines_number)

# 14 ? to check
amount_originally_deposited = float(input("Enter amount_originally_deposited: "))
annual_interest_rate = float(input("Enter annual_interest_rate: "))
compound_number = float(input("Enter compound_number: "))
number_of_years = float(input("Enter number_of_years: "))

amount_of_money_after_years = amount_originally_deposited*(1+(annual_interest_rate/compound_number)) ** (compound_number*number_of_years)

print("amount_of_money_after_years is ", amount_of_money_after_years)

# 15
