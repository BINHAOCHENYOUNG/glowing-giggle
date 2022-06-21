def main():
    #create a bool variable to use as a flag
    found = False
    #Get the search value (Enter the coffee name that you want to find)
    search_value = input("What do you want to search: ")
    #open the coffee.txt file 
    coffee_file = open('coffee.txt', 'r')
    #read the first record's name filed
    name = coffee_file.readline()
    #read the rest of the information using while
    while name != '':
        #read the description 
        descr = coffee_file.readline()
        #read quantity
        qty = coffee_file.readline()
        #read price
        price = coffee_file.readline()
        #strip
        name =name.rstrip("\n")
        descr =descr.rstrip("\n")
        qty = qty.rstrip("\n")
        price = price.rstrip("\n")
        #determin whether this records matches the search value or not
        if name == search_value:
            #Display the record
            print("name", name)
            print("description",descr)
            print("quantity", qty)
            print("price", price)
            #set the found flag to True
            found = True 
        #read next name of coffee
        name = coffee_file.readline()
    #close the file
    coffee_file.close() 
    #if your  search value is not matched or founded in the file , display a message
    if not found:
        print("We fail to find your search()")

main()