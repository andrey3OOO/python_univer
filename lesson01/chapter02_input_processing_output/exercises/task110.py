# 10
sugar_for_one_cookie = 1.5/48
butter_for_one_cookie = 1/48
flour_for_one_cookie = 2.75/48

cookies_count = int(input("Enter cookies count you want: "))
print("You need sugar: ", format(sugar_for_one_cookie*cookies_count, '.2f'))
print("butter: ", format(butter_for_one_cookie*cookies_count, '.2f'))
print("flour: ", format(flour_for_one_cookie*cookies_count, '.2f'))

