import itertools

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

compare = m - nums[0] - nums[1] - nums[2]
ans = 0

for i in itertools.combinations(nums, 3):
    new = m - sum(list(i))
    if new >= 0 :
        if new < compare:
            compare = m - sum(list(i))
            ans = sum(list(i))

print(ans)