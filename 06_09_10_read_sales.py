def main():
    sales_file = open("sales.txt","r")
    line = sales_file.readline()
    #As long as an empty string is not naturened from readline, continue processing
    while line != '':
        amount = float(line)
        print(f'{amount:,.2f}')
        line = sales_file.readline()
    sales_file.close()


main()