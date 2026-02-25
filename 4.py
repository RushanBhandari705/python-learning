Employee=str(input("Enter the employee's name:"))
Employee_Salary=float(input("Enter the employee's salary"))
Allowance=Employee_Salary*0.1
print("Your allowance is:", Allowance)
Tax=Employee_Salary*0.05
print("Your tax amount is:", Tax)
net_Salary=Employee_Salary+Allowance-Tax
print("Your netSalary is:", net_Salary)
