import math

print("Continuous Interest Calculator")

p0 = float(input("Enter initial investment amount: "))
t = float(input("Enter number of years invested: "))
r = float(input("Enter annual interest rate as a decimal: "))

pt = p0 * math.exp(r * t)

print("Final investment value =", pt)
