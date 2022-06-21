def main():
    print("Input two numbers")
    n1 = int(input("Enter 1st number"))
    n2 = int(input("Enter 2nd number"))
    show_sum(n1,n2)

def show_sum(num1,num2):
    result = num1 + num2
    print("The sum is", result)
main()