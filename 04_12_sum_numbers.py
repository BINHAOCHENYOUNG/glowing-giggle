# This program calculate sum of a series of numbers entered by the user 

#set the max number 
max = 10
#initialize an accumulator variable 
total = 0
#Explain what we are doing 
print('This program caculates the number of', max, 'numbers you will enter')
print
#Get the numbers and accumulate them 
for counter in range(max):
    number= int(input('Enter a number: '))
    total += number
#display the total of the number
print('the total is', total)
