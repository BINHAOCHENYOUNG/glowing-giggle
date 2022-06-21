# This program gets three test score from user and displays their average of the three exam score. And if the average is higher than the high score that you set up(95), then display the average with congreatulation message.

#get the high score
high_score = 95
#Get the user's name 
user_name =input("What is your name?: ")
#Get three exam score from user 
score_1 =float(input("what is your first score?: ")) 
score_2 =float(input("what is your second score?: "))
score_3 =float(input("what is your third score?: "))
#Calculate the average of the three exam score
average_score = (score_1 + score_2 + score_3)/3
#Print average score 
print(f"Your average score is, {average_score:,.2f}")
#Compare to the high score and if the average score is higher than your high socre display congreatulation message
if high_score <= average_score:
    print("Congratulation", user_name, "Your score is the above the high score")
else:
    print("Sorry", user_name, "you have to try better next time")
