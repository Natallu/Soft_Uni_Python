account_balance = 0
deposit = 0

while deposit != 'NoMoreMoney':
    deposit = input()
    if deposit == 'NoMoreMoney':
        break
    else:
        deposit = float(deposit)
        if deposit > 0:
            account_balance += deposit
            print(f'Increase: {deposit:.2f}')
        elif deposit <= 0:
            print('Invalid operation!')
            break

print(f'Total: {account_balance:.2f}')
