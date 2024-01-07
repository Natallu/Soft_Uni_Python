sq_meters = float(input())

total_cost = sq_meters * 7.61
discount_amount = total_cost * 0.18
final_price = total_cost - discount_amount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_amount} lv.")
