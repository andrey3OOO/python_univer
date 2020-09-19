# 14 ? to check
amount_originally_deposited = float(input("Enter amount_originally_deposited: "))
annual_interest_rate = float(input("Enter annual_interest_rate: "))
compound_number = float(input("Enter compound_number: "))
number_of_years = float(input("Enter number_of_years: "))

amount_of_money_after_years = amount_originally_deposited*(1+(annual_interest_rate/compound_number)) ** (compound_number*number_of_years)

print("amount_of_money_after_years is ", amount_of_money_after_years)

# 15a