#This following is using as a global constant the contribubtion rate and calculate how muc each gross pay and bonus is contribute to the retirement fund 


#Set CONTRIBUTION_RATE as global variable as 0.05
CONTRIBUTION_RATE=0.05
#Define main function to get input of gross pay and bonus, then calling show_pay_contrib function and show_bonus_contrib function 
def main():
    gross_pay = float(input('Enter your gross pay: '))
    bonus = float(input('Enter your bonus: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

#show_pay_contrib function calculate contribution of gross pay
def show_pay_contrib(pay):
    contrib = pay * CONTRIBUTION_RATE 
    print(f'Contribution for gross pay ${contrib:,.2f}')
#show_bonus_contrib function calculate contribution of bonus 
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE 
    print(f'Contribution for gross bonus ${contrib:,.2f}')
main()
