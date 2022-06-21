def main():
    #open the sales.txt
    sales_file = open("sales.txt","r")
    for line in sales_file:
        amount = float(line)
        print(f"{amount:,.2f}")
    sales_file.close()

main()