budget = float(input())
ticket_type = input()
people = int(input())

vip_ticket = 499.99
normal_ticket = 249.99

transport = 0

if people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.6
elif 10 <= people <= 24:
    transport = budget * 0.5
elif 25 <= people <= 49:
    transport = budget * 0.4
elif people >= 50:
    transport = budget * 0.25

money_for_tickets = budget - transport

ticket_price = 0

if ticket_type == 'VIP':
    ticket_price = people * vip_ticket
elif ticket_type == 'Normal':
    ticket_price = people * normal_ticket

diff = abs(money_for_tickets - ticket_price)

if money_for_tickets >= ticket_price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
