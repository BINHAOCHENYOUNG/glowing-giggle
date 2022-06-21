# This program allows the user to modify the quantity in a record in the coffee.txt file 

import os 

def main():
    found  = False
    search = input("Enter a name to of a coffee for search: ")
    new_price = int(input('Enter the new retail price: '))
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt','w')
    name = coffee_file.readline()
    while name != '':
        descr = coffee_file.readline().rstrip('\n')
        qty = coffee_file.readline().rstrip('\n')
        price = coffee_file.readline().rstrip('\n')
        name=name.rstrip('\n')
        if name == search:
            temp_file.write(name + '\n')
            temp_file.write(descr+ '\n')
            temp_file.write(str(qty) +'\n')
            temp_file.write(str(new_price) + '\n')
            found = True 
        name = coffee_file.readline()
    coffee_file.close()
    temp_file.close()
    os.remove('coffee.txt')
    os.rename('temp.txt','coffee.txt')
    if found:
        print('The file has been updated')
    else:
        print('That item was not found in the file')

main()
        