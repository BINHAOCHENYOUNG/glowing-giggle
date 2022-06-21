# This program uses a loop display a table of numbers and their squares

# Get the starting value 

#Get the end value 

start = int(input("Enter the starting number: "))

end = int(input("Enter the end number: "))

print()
print("Numbers\tSquare")
print("---------------")

#Display the numbers and thier squares 
for number in range(start,end+1):
    square = number **2
    print(number, "\t", square)
