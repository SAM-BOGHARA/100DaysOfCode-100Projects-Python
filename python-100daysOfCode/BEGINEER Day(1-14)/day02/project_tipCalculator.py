bill = float(input("What was total bill?\n $"))
tip = int(input("What percentage tip would you like to give ? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
total_tip = bill * tip / 100
total_bill = bill + total_tip
result = total_bill / people
print("Each one has to pay : " ,round(result,2))
