#This program promts the user for sales amoount and writes those amounts to the sales.txt. At the begining we will ask how many months for recoding sales.

def main():
    #get a number of days  for sales records
    num_days = int(input("How many days do you have: "))
    #open a new file named sales.txt 
    sales_file = open("sales.txt", "w")

    
    #get the amount of sales for each day and write it to the file 
    for count in range(1, num_days+1):
        #get the sales for  day 
        sales = float(input("Enter the sales for day #" + str(count) + ":" ))
        #write sales amount to the file 
        sales_file.write(str(sales)+'\n')
         

    #close the file 
    sales_file.close()
    print("Data was written to sales.txt")
    

main()
    
