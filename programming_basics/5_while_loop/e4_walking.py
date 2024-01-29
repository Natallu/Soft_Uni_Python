data = input()

goal_steps = 10000
steps = 0

while data != 'Going home':
    current_steps = int(data)

    steps += current_steps

    if steps >= goal_steps:
        break

    data = input()

if data == 'Going home':
    data = int(input())
    steps += data

diff = abs(steps - goal_steps)
if steps > goal_steps:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
elif steps < goal_steps:
    print(f'{diff} more steps to reach goal.')
