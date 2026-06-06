print("House Affordability Calculator")

d = float(input("Enter monthly payment you can afford: "))
r = float(input("Enter annual interest rate as a decimal: "))

k = 12

n15 = 15
n30 = 30

p15 = d * ((1 - (1 + r / k) ** (-n15 * k)) / (r / k))
p30 = d * ((1 - (1 + r / k) ** (-n30 * k)) / (r / k))

print("Loan amount for 15-year mortgage =", p15)
print("Loan amount for 30-year mortgage =", p30)
