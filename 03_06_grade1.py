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
else:
    if score >= B_Score:
        print("your grades is B")
        print(f"you need {A_Score - score} more score to get A")
    else:
        if score >=C_Score:
            print("Your grades is C")
            print(f"you need {A_Score - score} more score to get A")     
        else:
            if score >=D_Score:
                print("Your grades is D")
                print(f"you need {A_Score - score} more score to get A")
            else:
                print("Your grades is F")
                print(f"you need {A_Score - score} more score to get A")