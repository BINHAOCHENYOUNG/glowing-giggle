# This program we will get salary from user and display whether he/she met the sales quota

sales = float(input("what is your sales total?: "))

if sales > 50000:
    bonus = 0.1 * sales
    print("you met your sales quota!!")
    print("your bonus is $", bonus)
    print(f"your total payment is ${sales +bonus:,.2f}")
else: 
    print("you'd better work hard")

