#This program gets three names from user and writes them to a file 

def main():
    name1= input("Write the first name: ")
    name2= input("Write the second name: ")
    name3= input("Write the third name: ")
    #open a file names friends.txt
    myfile = open("friends.txt","w")
    #Write the name to file 
    myfile.write(name1+'\n')
    myfile.write(name2+'\n')
    myfile.write(name3+'\n')    
    myfile.close()

    print("The name were written to friends.txt")

main()