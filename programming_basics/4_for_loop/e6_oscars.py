actors_name = input()
academy_points = float(input())
n_voters = int(input())

for _ in range(n_voters):
    voter_name = input()
    points_given = float(input())
    academy_points += len(voter_name) * points_given / 2
    if academy_points > 1250.5:
        print(f'Congratulations, {actors_name} got a nominee for leading role with {academy_points:.1f}!')
        break
else:
    diff = 1250.5 - academy_points
    print(f'Sorry, {actors_name} you need {diff:.1f} more!')
