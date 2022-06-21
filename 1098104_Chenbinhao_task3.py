DISCOUNT =0.12
def main():
    regular_price = float(input("Enter the item's regular price: "))
    sales_price = regular_price *(1-DISCOUNT)
    print(f"The sale price is ${sales_price:,.2f}")


main()