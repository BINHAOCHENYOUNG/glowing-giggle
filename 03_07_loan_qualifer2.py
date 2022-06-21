#This program determine whether a bank customer is qualified for a loan. There are two conditions for loan. First is customer's annual salary should over 60,000 yuan and the year of current job should be mroe than 3 years

#Set the condition 1 and 2
##mminimum annual salary is greater than 60,000
Min_SALARY = 30000
##minimum year of works with current company should more than 3 years
Min_Years = 2
#Get customer information (condition)
##Get the customer's annual salary 
salary = float(input("Enter your annual salary: "))
##Get the customer's year of works
years_on_job = float(input("Enter your years of work: "))

if salary >= Min_SALARY and years_on_job >= Min_Years:
    print("You qualify for the loan")
else:
    print("You do not qalify for this loan")

