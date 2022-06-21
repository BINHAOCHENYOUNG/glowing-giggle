def main():
    infile = open("employee.txt","r")
    
    
    name = infile.readline()
    while name !='':
        name=name.rstrip()
        print('Name: ', name)
        id_num =infile.readline()
        Dep = infile.readline()
        Dep=Dep.rstrip()
        print("Dept: ", Dep)
        name=infile.readline()
        print()
    infile.close()
    
main()