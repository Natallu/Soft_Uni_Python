from math import pi

r = float(input())

parameter = 2 * pi * r
area = pi * (r ** 2)

calculated_area = f"{area:.2f}"
calculated_parameter = f"{parameter:.2f}"

print(calculated_area)
print(calculated_parameter)
