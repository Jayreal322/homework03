print("Monthly Deposit Calculator")

goal = float(input("Enter desired down payment amount: "))
r = float(input("Enter annual interest rate as a decimal: "))

k = 12
months = 24

d = goal * (r / k) / (((1 + r / k) ** months) - 1)

print("Required monthly deposit =", d)
