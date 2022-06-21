#This program will give a menu that gove a choice of analysis(anrea, circumference, area, perimeter, circle)
import mycircle
import myrect

def main():
    choice = 0 
    while choice != 5:
        display_menu()
        choice =int(input("Enter your choice(1~5)"))
        if choice == 1:
            radius = float(input("Enter the radius of the circle:"))
            print('The area is', f"{mycircle.area(radius):,.2f}")
        elif choice == 2:
            radius = float(input("Enter the radius of the circle:"))
            print('The circumference is', f"{mycircle.circumference(radius):,.2f}")
        elif choice == 3:
            width = float(input("Enter the with of the circle:"))
            length = float(input("Enter the length of the circle:"))
            print('The area is', f"{myrect.area(width, length):,.2f}")
        elif choice == 4:
            width = float(input("Enter the with of the circle:"))
            length = float(input("Enter the length of the circle:"))
            print('The perimeter is', f"{myrect.perimeter(width,length):,.2f}")
        elif choice == 5:
            print('Exiting the program')
        else:
            print("Error: invalid selection")

# User choice

def display_menu():
    print("[[Menu]]")
    print("(1) Area of a circle")
    print("(2) Circumcumference of a circle")
    print("(3) Area of a rectangle")
    print("(4) Perimeter of a rectangle")
    print("(5) quit")

main()