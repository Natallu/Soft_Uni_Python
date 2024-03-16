tournament_stage = input()
ticket_type = input()
number_of_tickets = int(input())
trophy_photo = input()

ticket_price = 0

if tournament_stage == "Quarter final":

    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90

elif tournament_stage == "Semi final":

    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40

elif tournament_stage == "Final":

    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400.00

total_price = number_of_tickets * ticket_price

if total_price > 4000:
    total_price *= 0.75

    if trophy_photo == "Y":
        total_price -= 40 * number_of_tickets

elif total_price > 2500:
    total_price *= 0.9

if trophy_photo == "Y" and total_price > 0:
    total_price += 40 * number_of_tickets

print(f"{total_price:.2f}")
