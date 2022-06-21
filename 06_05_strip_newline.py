#This program reads the contents from file and remove the linebreak 

def main():
    infile = open("friends.txt","r")
    line1 = infile.readline().rstrip("\n")
    line2 = infile.readline()
    line3 = infile.readline()
   
    infile.close()
    print(line1)
    print(line2)
    print(line3)

main()