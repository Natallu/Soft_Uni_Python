students = int(input())

fail = 0
between_3_4 = 0
between_4_5 = 0
top = 0
total = 0

for _ in range(students):
    grade = float(input())
    total += grade
    if 2 <= grade <= 2.99:
        fail += 1
    elif 3 <= grade <= 3.99:
        between_3_4 += 1
    elif 4 <= grade <= 4.99:
        between_4_5 += 1
    else:
        top += 1

fail_percent = fail / students * 100
between_3_4_percent = between_3_4 / students * 100
between_4_5_percent = between_4_5 / students * 100
top_percent = top / students * 100

average_grade = total / students

print(f'Top students: {top_percent:.2f}%')
print(f"Between 4.00 and 4.99: {between_4_5_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_4_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
