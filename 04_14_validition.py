# This pragram will validate the user's input 

score = int(input('Enter a test score: '))

#Make sure it is not less than 0
while score <0:
    print('ERROR: The score cannot be negative value')
    score = int(input('Enter a correct test score: '))
    