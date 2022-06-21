#This program converts cups to fluid ounces
CUPSFOROUNCES = 8

def main():
    intro()
    cupts_needed = int(input("Enter the number of cups: "))
    cups_to_ounces(cupts_needed)

def intro():
    print("This program converts measurements in cups to fluid onuces. For your reference the formula is: 1 cup = 8 fluid ounces")

def cups_to_ounces(cupts):
    ounces = cupts * CUPSFOROUNCES
    print("That converts to", ounces, "ounces.")

main()