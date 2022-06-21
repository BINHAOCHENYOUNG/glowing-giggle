#This program gets an item's original price and calculates its sale price, with a 25% discunt 
discount_rate = 0.25
# get a item's original price 
original_price = float(input("What is the price?: "))
#calculate discount 
discount = original_price * discount_rate
#calculate sales price
sales_price = original_price - discount
#display output
print("Your original price is" , original_price)
print("You save", discount, "yuan")
print("Your sales price is", sales_price)

