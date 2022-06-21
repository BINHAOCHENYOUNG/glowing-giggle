#This program will calculate the future value of your investment

#Get the desired future value 
future_value = float(input("Please, enter he desired future value: "))
#Get the annual interest rate 
rate = 0.0236
#Get the number of years that the money will appreciates 
year = 10
#calculate the amount you need to deposit 
present_value = future_value/(1 + rate)**year
#Display the result
print(f"you will need to deposit this amount: ${present_value:,.2f} ")

