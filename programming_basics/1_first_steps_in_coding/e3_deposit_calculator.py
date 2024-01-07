deposit_amount = float(input())
period_in_months = int(input())
year_interest_rate = float(input())

interest_rate = year_interest_rate / 100

interest_rate_total = deposit_amount * interest_rate
interest_rate_monthly = interest_rate_total / 12

amount_end_of_deposit = deposit_amount + period_in_months * interest_rate_monthly

print(amount_end_of_deposit)
