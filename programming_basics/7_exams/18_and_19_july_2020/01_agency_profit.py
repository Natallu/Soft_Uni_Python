avio_company = input()
adult_tickets = int(input())
children_tickets = int(input())
net_ticket_price_adult = float(input())
service_price = float(input())

net_ticket_price_children = net_ticket_price_adult - 0.7 * net_ticket_price_adult
total_adults = adult_tickets * (net_ticket_price_adult + service_price)
total_children = children_tickets * (net_ticket_price_children + service_price)

profit = (total_children + total_adults) * 0.2

print(f'The profit of your agency from {avio_company} tickets is {profit:.2f} lv.')
