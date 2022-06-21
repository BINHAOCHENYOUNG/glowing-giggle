#This program will read sales.txt file and display it 

from abc import ABCMeta


def main():
    #open the sales.txt
    sales_file = open("sales.txt","r")
    #read first line from the file 
    line = sales_file.readline()
    #while it meet with empty string"""
    while line != '': 
        #convert contents in line to float
        amount = float(line)
        #Display the line from the file 
        print(f'{amount:,.2f}')
        #read next line
        line = sales_file.readline() 
    #close the file 
    sales_file.close()

main()