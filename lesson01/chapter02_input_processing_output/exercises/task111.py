# 11
male_count = int(input("Enter male count: "))
female_count = int(input("Enter female count: "))
male_index = male_count/(male_count+female_count)
female_index = female_count/(male_count+female_count)
print("Male index is: ", format(male_index, '.1f'))
print("Female index is: ", format(female_index, '.1f'))

