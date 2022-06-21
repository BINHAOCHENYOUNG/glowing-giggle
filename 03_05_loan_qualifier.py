#This program determine whether a bank customer is qualified for a loan. There are two conditions for loan. First is customer's annual salary should over 60,000 yuan and the year of current job should be mroe than 3 years

#Set the condition 1 and 2
##mminimum annual salary is greater than 60,000
Min_SALARY = 60000
##minimum year of works with current company should more than 3 years
Min_Years = 3
#Get customer information (condition)
##Get the customer's annual salary 
salary = float(input("Enter your annual salary: "))
##Get the customer's year of works
year = float(input("Enter your years of work: "))
# determined whether the customer is qualified 
if salary >= Min_SALARY:
    if year >=Min_Years:
        print("You qualify for the loan")
    else:
        print("You need", Min_Years, "Years to qualify")
else:
    print("You must earn at least", f'{Min_SALARY:,.2f}', "yuan to qualify")