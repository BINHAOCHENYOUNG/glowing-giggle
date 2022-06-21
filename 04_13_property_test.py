#This program display property taxes

#Get the tax_factor
tax_factor=0.0075
#get the lot number
lot = int(input('lot number: '))
#Continue processing as long as theuser does not enter lot number 0 
while lot !=0:
    #get the property value
    value = float(input('Enter the property value: '))
    #Calculate the property tax
    tax = value * tax_factor
    #Display the tax 
    print(f'property tax: ${tax:,.2f}')
    #Get the next lot numbber 
    print('Enter the next lot number or enter 0 to end')
    lot = int(input('Lot number: '))
    