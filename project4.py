total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid by the customer: "))


due_amount = total_bill - amount_paid

if due_amount > 0:
    print(f"The customer still owes: ${due_amount:.2f}")
elif due_amount == 0:
    print("The bill has been fully paid. No due amount.")
else:
    print(f"Overpaid by: ${-due_amount:.2f} (refund or credit due to customer)")
