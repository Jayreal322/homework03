print("Mortgage Payment Calculator")

p0 = float(input("Enter loan amount: "))
r = float(input("Enter annual interest rate as a decimal: "))
n = float(input("Enter loan term in years: "))

k = 12

d = p0 / ((1 - (1 + r / k) ** (-n * k)) / (r / k))

print("Monthly payment =", d)
