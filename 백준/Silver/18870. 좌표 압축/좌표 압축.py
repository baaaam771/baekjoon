n = int(input())
nums = list(map(int, input().split()))
# print(nums)
sorted_nums = sorted(nums)
# print(sorted_nums)
num_dict = {}
index = 0
for i in sorted_nums:
    if i not in num_dict:
        num_dict[i] = index
        index += 1
# print(num_dict)

ans = []
for i in nums:
    ans.append(num_dict[i])

print(' '.join(map(str, ans)))