#THis program will writes three lines of your friends names to a file 

def main():
    outfile = open("friends.txt","w")
    outfile.write("Chenyu Huang\n")
    outfile.write("Xinyue Peng\n")
    outfile.write("Li Liu\n")
    outfile.close()


main()