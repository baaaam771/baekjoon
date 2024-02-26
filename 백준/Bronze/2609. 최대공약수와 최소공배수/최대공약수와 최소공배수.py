nums = list(map(int, input().split()))
a, b = nums[0], nums[1]

while a != 0:
    a, b = b, a % b
    if b == 0:
        print(a)
        break

print(nums[0] * nums[1] // a)