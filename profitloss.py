actual_cost=(float(input("Enter the actual amt: ")))
sale_cost=(float(input("Enter the sale amt: ")))
amt=actual_cost-sale_cost
if (sale_cost<actual_cost):
    print("the profit is: ",amt)
else:
    print("the loss is: ",amt)
