# 6
purchase_sum = int(input("Enter purchase sum: "))
fed_tax = purchase_sum * 0.05
reg_tax = purchase_sum * 0.025
print("Federal tax = ", fed_tax)
print("Regional tax = ", reg_tax)
print("Total tax = ", fed_tax+reg_tax)
print("Total = ", purchase_sum+fed_tax+reg_tax)

