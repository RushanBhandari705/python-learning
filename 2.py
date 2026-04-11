
Item1= str(input("Enter the name of the item1:"))
Item1_Price=float(input("Enter the price of item1"))
Item2=str(input("Enter the name of the item2:"))
Item2_Price=float(input("Enter the price of item2:"))
Item3=str(input("Enter the name of item3:"))
Item3_Price=float(input("Enter the price of item3:"))
Total_Cost=Item1_Price+Item2_Price+Item3_Price
print("The total cost is:", Total_Cost)
Tax=Total_Cost*0.13
Total_After_Tax= Tax+Total_Cost
print("The total after tax is:", Total_After_Tax)
