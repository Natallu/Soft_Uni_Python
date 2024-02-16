from math import ceil

visitors = int(input())
entrance_tax = float(input())
lounger = float(input())
umbrella = float(input())

entrance_fee = visitors * entrance_tax
umbrellas_needed = ceil(visitors / 2)
umbrellas_fee = umbrella * umbrellas_needed
loungers_needed = ceil(visitors * 0.75)
loungers_fee = lounger * loungers_needed

total_price = entrance_fee + umbrellas_fee + loungers_fee

print(f'{total_price:.2f} lv.')
