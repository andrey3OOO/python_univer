# 12
PURCHASED_STOCKS = 2000
PURCHASED_PRICE = 40
TAX = 0.03
SOLD_STOCKS = 2000
SOLD_PRICE = 42.75

purchase_sum = PURCHASED_STOCKS*PURCHASED_PRICE
purchase_tax = purchase_sum*TAX
purchase_total = purchase_sum + purchase_tax
sold_sum = SOLD_STOCKS*SOLD_PRICE
sold_tax = sold_sum*TAX
sold_total = sold_sum + sold_tax


print("Purchase total is ", purchase_total)
print("Purchase tax is ", purchase_tax)

print("Sold total is ", sold_total)
print("Sold tax is ", sold_tax)

print("Profit is ", sold_total-purchase_total)

