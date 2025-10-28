def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * tip_percentage / 100
    return tip

def calculate_total(bill_amount, tip):
    total = bill_amount + tip
    return total

def printBill(total_tip, total_bill):
    print("\n|----------- Bill -----------|")
    print(f"     Total tip: ₱{total_tip}")
    print(f"     Total bill: ₱{total_bill}")
    print("|----------------------------|")