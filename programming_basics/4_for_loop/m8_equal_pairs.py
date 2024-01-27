number_pairs = int(input())
pair_sum = int(input()) + int(input())
max_diff = 0

for pairs in range(number_pairs -1):
    current_sum = int(input()) + int(input())
    diff = abs(pair_sum - current_sum)
    if diff > max_diff:
        max_diff = diff

    pair_sum = current_sum

if max_diff == 0:
    print(f'Yes, value={pair_sum}')
else:
    print(f'No, maxdiff={max_diff}')
