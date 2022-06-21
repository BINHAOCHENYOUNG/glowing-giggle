#This program compares strings with the < operator 

#Get two names from the user 
name1 =input("Enter first person's name: ")
name2 =input("Enter second person's name: ")

#Display the names in a alphabetical order
print("Here are the names, Listed alphabetically")
if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)

