number = int(input())
nums = 1

while nums <= number:
    print(nums)
    nums = nums * 2 + 1
    if nums > number:
        break
