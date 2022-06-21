# This program adds coffee inventory records to the coffee.txt file 
def main():

# Create a variable to control the loop 
    another = 'y'

# open the coffee.txt in append mode 
    coffee_file =  open('coffee.txt', 'a')
#add records to the file using "while"
    while another == 'y' or another =='Y':
    #get the coffee record data 
        print('Enter the follow coffee data')
        name =  input('Name: ')
        descr = input("Description: ")
        qty = int(input("Quantity: "))
        price = int(input("Price: "))

    #append the data to the file 
        coffee_file.write(name +'\n')
        coffee_file.write(descr+'\n')
        coffee_file.write(str(qty)+'\n')
        coffee_file.write(str(price)+'\n')
    #determine whether the user want to add another record to the file 
        print("Do you want to add another records")
        another = input('Y or y for yes, anything else for no')
# close the file 
    coffee_file.close()
#call the main
main()