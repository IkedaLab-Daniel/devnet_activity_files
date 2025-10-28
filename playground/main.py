import tip_calculator

# > 1.1 User input data
bill_amount = float(input("Enter bill amount: ₱"))
tip_percentage = float(input("Enter tip percentage: "))

# > 1.2. Validate percentage (no negative dapat)
if (tip_percentage > 0):

    # > 2. Calculations
    total_tip = tip_calculator.calculate_tip(bill_amount, tip_percentage)
    total_bill = tip_calculator.calculate_total(bill_amount, total_tip)

    # > 3. Display result
    tip_calculator.printBill(total_tip, total_bill)

else:
    print("No negative tipping please!!! >:(")