#This program calculates a salesperson's pay at a company
# 10000>=0.10, 15000>= 0.12, 20000>=0.14, 25000>=0.16, 30000>=0.18
def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determined_comm_rate(sales)
    pay = sales *comm_rate -advanced_pay
    print("You pay in this mont is $", pay)
    if pay < 0:
        print("You saleperson must reimburse the company")

def get_sales():
    monthly_sales = float(input("Enterthis month sales amount: "))
    return monthly_sales

def get_advanced_pay():
    adv_pay = float(input("Enter your advance payment: "))
    return adv_pay

def determined_comm_rate(sales):
    if sales < 10000:
        rate = 0.10
    elif sales >=10000:
        rate = 0.12    
    elif sales>= 15000:
        rate =0.14
    elif sales >=20000:
        rate = 0.16
    elif sales >=25000:
        rate = 0.18
    else:
        rate = 0.18
    return rate

main()
