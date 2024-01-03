def total_with_tip(bill, percentage):
    if bill < 0:
        raise ValueError("Bill cannot be negative")
    if percentage > 100:
        raise ValueError("Percentage cannot be greater than 100%")
    if percentage < 0:
        raise ValueError("Percentage cannot be negative")
    
    tip = bill * percentage / 100
    if tip > 500:
        tip = 500
    
    total = bill + tip
    if total < 5:
        total = 5
    return round(total, 2)