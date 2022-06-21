def main():
    #open a file for writing
    outfile = open("number.txt","w")
    #get three numbers from the user
    num1= int(input("Write the first number: "))
    num2= int(input("Write the second number: "))
    num3= int(input("Write the third number: "))
    #write the numbers to the file 
    outfile.write(str(num1) +'\n')
    outfile.write(str(num2) +'\n')
    outfile.write(str(num3) +'\n')
    #close the file 
    outfile.close()
    #display a message that contents are written in a file 
    print("The numbers have been written into the file")


main()