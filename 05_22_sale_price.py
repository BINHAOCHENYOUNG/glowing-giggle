#this program calculate a retail item's sale price.

# Set DISCOUNT_PERCENTAGE as 25%
DISCOUNT_PERCENTAGE = 0.25
#The main function
def main():
    #Get the item's regular price 
    regular_price = get_regular_price()
    #Calculate the discount
    sale_price = regular_price - discount(regular_price)
    #Display the sale price 
    discount2 = discount(regular_price)
    print("The regular price is", regular_price)
    print("The discount amount is", discount2)
    print("The discounted price is", sale_price)

def get_regular_price():
    price = float(input("Enter the regular price: "))
    return price

def discount(regular_price):
    discount = regular_price * DISCOUNT_PERCENTAGE
    return discount 

#Call the function
main()