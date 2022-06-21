def main():
    infile = open("friends.txt","r")
    contents = infile.read()
    infile.close()
    print(contents)

main()