#This program calculate retail price 
Mark_up = 2.5
another ='y'
while another =='y' or another =='Y':
    #get the item's wholesale cost 
    wholesale = float(input("Enter the item's wholesale cost:"))
    #calculate the retail price
    #validation the wholesale cost 
    while wholesale < 0:
        print('ERROR: The cost cannot be negative')
        wholesale = float(input("Enter the correct item's wholesale cost: "))
    retail = wholesale *Mark_up
    #display the retail price 
    print(f'retail price: ${retail:,.2}')
    #Do this again
    another =  input('Do you have another item? (Enter y or Y for yes): ')