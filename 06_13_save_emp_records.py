#This program gets employee data from the user and saves it as records n the employee.txt file 


def main():
    num_emp =int(input('How mant employee records do you want to create? '))
    emp_file = open('employee.txt','w')
    for count in range (1,num_emp+1):
        name = input("Name: ")
        id_num = input("ID Number: ")
        dept= input('Department: ')
        emp_file.write(name+ '\n')
        emp_file.write(id_num+ '\n')
        emp_file.write(dept+ '\n')
        #Blank Line
        print()
    emp_file.close()
    print('The employee data are recoreded to the file')
main()