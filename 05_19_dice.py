#This program will simulate rolling of dice 

import random 

MIN=1
MAX=6

def main():
    again = "y"
    while again == "Y" or again == "y":
        print("Rolling dice")
        value = random.randint(MIN,MAX)
        print(f"You have {value}")
        input("Hit enter for computer's turn")
        print("Computer rolling dice")
        comp_value = random.randint(MIN,MAX)
        print(f'Computer have {comp_value}')
        if value < comp_value:
            print("You loss the game")
        elif value == comp_value:
            print("Same")
        else:
            print("You win the game")
        again = input('Roll them again?(y or Y for yes):')

main()