actual_amount = int(input("Please enter the original price:"))
sale_amount = int(input("Please enter the sale price"))

if sale_amount > actual_amount:
    profit = sale_amount - actual_amount
    print("Making profit. profit made:", profit)
else:
    print("No profit made.")
        