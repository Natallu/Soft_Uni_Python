bitcoins = int(input())
chinese_yuan = float(input())
commission = float(input()) / 100

bitcoin_to_bgn = bitcoins * 1168
chinese_yuan_to_dollars = chinese_yuan * 0.15
dollars_to_bgn = chinese_yuan_to_dollars * 1.76
total_bgn = bitcoin_to_bgn + dollars_to_bgn
total_euro = total_bgn / 1.95

total_euro_after_commission = total_euro - (total_euro * commission)

print(f"{total_euro_after_commission:.2f}")
