import math

num_kozunaks = int(input())

total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0

for _ in range(num_kozunaks):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    if sugar > max_sugar:
        max_sugar = sugar

    if flour > max_flour:
        max_flour = flour

sugar_packs = math.ceil(total_sugar / 950)
flour_packs = math.ceil(total_flour / 750)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
