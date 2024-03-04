yearly_tax_basketball = int(input())

snickers = yearly_tax_basketball - 0.4 * yearly_tax_basketball
basketball_clothes = snickers - 0.2 * snickers
ball = basketball_clothes * 1/4
basketball_accessories = ball * 1/5

total_cost = snickers + basketball_accessories + basketball_clothes + ball + yearly_tax_basketball

print(f'{total_cost:.2f}')
