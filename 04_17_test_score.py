#this program averages the test score. it asks the user fot the number of students and the number of test score per student

#get the number of students
num_students = int(input('How many students do you have: '))
#Get the number of test socres per student 
num_test_score = int(input('How many test scores per student? '))
#Determine each student's averae test score
for student in range (num_students):
    #set the initialization value for the test score
    total = 0.0
    #get a student's test score 
    print('Student number', student+1)
    print('-------------------------')
    for test_number in range (num_test_score):
        #Get the test score for each student
        print('Test number', test_number+1)
        #add th esocre to the accumulator 
        score = float(input(': '))
        total += score
    #calculate the average test score for this student 
    average = total / num_test_score
    #display the average 
    print('The average test score for this student', student+1, "is: ", average)
    print()
