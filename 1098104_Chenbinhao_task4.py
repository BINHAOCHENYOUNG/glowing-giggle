def main():
    num_emp = int(input("How many employee records do you want to create: "))
    employee_file = open("employee.txt", "w")


    for count in range(1, num_emp+1):
        print("Enter data for employee #" + str(count))
        name = input("Name: ")
        id_num = input("ID Number: ")
        dep=input("Department: ")
        
        employee_file.write(name+ '\n')
        employee_file.write(id_num + '\n')
        employee_file.write(dep + '\n')
        print()
        

    #close the file 
    employee_file.close()
    print("Employee records written to employee.txt")

main()