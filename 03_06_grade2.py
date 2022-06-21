#This program gets a numeric test score form the user and displays the cooresponding letter grade. 


# Named constants to represent the grade threshods

A_Score = 90
B_Score = 80
C_Score = 70
D_Score = 60

#Get the score 
score = int(input("Enter your test score: "))

#Determined the grade
if score >= A_Score:
    print("Your grade is A")
elif score >= B_Score:
    print("Your grade is B")
elif score >= C_Score:
    print("Your grade is C")
elif score >= D_Score:
    print("Your grade is D")
else: 
    print("Your grade is F")
