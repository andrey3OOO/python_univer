# 2
purchase_sum = int(input("Enter purchase sum: "))
global reg_tax
global fed_tax


def calc_fed_tax():
    fed_tax = purchase_sum * 0.05
    print(fed_tax)


def calc_reg_tax():
    reg_tax = purchase_sum * 0.025
    print(reg_tax)


def calc_total_tax():
    print(fed_tax+reg_tax)

calc_fed_tax()
calc_reg_tax()
#
# print("Federal tax = ", fed_tax)
# print("Regional tax = ", reg_tax)
# print("Total tax = ", fed_tax+reg_tax)
# print("Total = ", purchase_sum+fed_tax+reg_tax)
