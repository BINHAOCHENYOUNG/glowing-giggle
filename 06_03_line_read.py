#This program read the contents of the text file from previous class(friends.txt) and read contents line by line 

def main():
    infile = open("friends.txt","r")
    line1= infile.readline()
    line2= infile.readline()
    line3= infile.readline()
    infile.close()
    print(line1)
    print(line2)
    print(line3)
    

main()