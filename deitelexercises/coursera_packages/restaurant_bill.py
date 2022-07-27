total_bill_ = 0


bill_amount = float(input("Enter bill amount "))
initial_sales_tax = float(input("enter sales tax"))
initial_percentage_tip = float(input("enter percentage tip"))


sales_tax = bill_amount * initial_sales_tax / 100
tip_percentage = bill_amount  * initial_percentage_tip / 100
total_bill_ = bill_amount + sales_tax + tip_percentage
print("The total bill is ",total_bill_)
