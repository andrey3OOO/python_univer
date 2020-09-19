# 8
charge = int(input("Enter food charge: "))
tax = charge*0.018
tip = charge*0.07
total = charge+tax+tip
print("Total is ", format(total, '.2f'))

