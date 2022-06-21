#this program uses the return value of a function 

def main():
    first_age = int(input("Enter fitst person's age"))
    second_age = int(input("Enter second person's age"))
    total = sum(first_age, second_age)
    print("Total ages of two individuals are", total)

def sum(num1,num2):
    result = num1 + num2
    return result 


main()
