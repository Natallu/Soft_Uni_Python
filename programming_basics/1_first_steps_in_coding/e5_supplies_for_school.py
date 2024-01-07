pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())

pens_total = pens * 5.80
markers_total = markers * 7.20
detergent_total = detergent * 1.20

total_amount = pens_total + markers_total + detergent_total
discount_total = total_amount * discount/100

final_price = total_amount - discount_total

print(final_price)
