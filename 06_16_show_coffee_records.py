def main():
    coffee_file = open("coffee.txt",'r')
    
    name = coffee_file.readline()
    while name != '' :
        descr = coffee_file.readline() 
        qty = coffee_file.readline()
        price = coffee_file.readline()
        name =  name.rstrip("\n")
        descr = descr.rstrip("\n")
        qty = qty.rstrip("\n")
        price = price.rstrip("\n")
        print("Name:",name)
        print("Description: ", descr)
        print("Quantity: ",qty)
        print("Price: ",price)
        name = coffee_file.readline()
    coffee_file.close()
main()
