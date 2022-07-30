# Welcoming Announcement.
print("Welcome to the tip calculator

# Get Total Bill
bill = float(input("What was the total bill? $"))

# Get Tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Get amount of people who will be splitting the bill.
people = int(input("How many people to split the bill? "))

# Calculations
tip_as_a_percent = tip / 100
total_tip_amount = bill * tip_as_a_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

# Final amount being calculated and rounded to the 2 decimal places.
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
