# This program demonstrate the keyword argument 


#define main function 
def main():
    show_interest(rate=0.01, periods =10, principal=10000.0)

def show_interest(rate, periods, principal):
    interest = principal * rate * periods
    print(f"The sime interest will be $ {interest:,.2f}")
    

main()