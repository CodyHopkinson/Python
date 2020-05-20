# (The amount of money you get every hour)
hourly_rate = float(input("What's your hourly rate?"))
hours_worked = int(input("How many hour do you work?"))

# (Adding hour rates and hours worked together)
wages = hourly_rate * hours_worked
print("your pay this week before tax is: ${} ".format(wages))

# (Take away 20% of the money they earn)
tax = wages * 0.8

# (The money thats left over)
final_wage = print("After tax @ 20% that is: ${}".format(tax))

# (The yearly pay)
income = wages * 52
yearly_pay = income * 0.8
print("This is the amount of money you would make in a year ${}".format(yearly_pay))

# (if your income is low or high)
if yearly_pay <= 23000:
    print("I would like a Big Mac please")
else:
    print("So your the big dog now!?")
