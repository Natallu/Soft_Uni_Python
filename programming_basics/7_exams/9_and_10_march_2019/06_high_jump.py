target_height = int(input())
current_height = target_height - 30
failed_jumps = 0
total_jumps = 0

while True:
    jump_height = int(input())
    total_jumps += 1

    if jump_height > current_height:
        current_height += 5
        failed_jumps = 0

    else:
        failed_jumps += 1

    if failed_jumps == 3:
        print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
        break

    if current_height > target_height:
        print(f"Tihomir succeeded, he jumped over {current_height - 5}cm after {total_jumps} jumps.")
        break
