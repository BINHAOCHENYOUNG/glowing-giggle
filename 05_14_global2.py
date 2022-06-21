#Create a global variable  
number =100

def main():
    number =int(input("Enter a number: "))
    show_number()

def show_number():
    print('The number you enter is', number)

main()