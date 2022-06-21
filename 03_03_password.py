# This program compare two strings and if the password is correct then give access.

#Set a password 
PW_Origin = "mgs3001"
#Get a password 
pw_input= input("Enter your password: ")
#Deterine whether the correct password was entered 
if pw_input ==PW_Origin:
##If correct display message ("Your password is correct")
    print("Your password is correct")
##If fale display message ("Your password is wrong")
else:
    print("Your password is wrong")

    