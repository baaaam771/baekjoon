n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

chk_dict = {}
for i in arr:
    if i in chk_dict:
        chk_dict[i] += 1
    else:
        chk_dict[i] = 1

nums = []
ans = []
def back(dep):
    if dep == m:
        ans.append(list(nums))
    for i in arr:
        if chk_dict[i] > 0 :
            chk_dict[i] -= 1
            nums.append(i)
            back(dep+1)
            chk_dict[i] += 1
            nums.pop()

back(0)
unique_set = set(tuple(sub) for sub in ans)

unique_list = [list(sub) for sub in unique_set]
unique_list.sort()
for i in unique_list:
    print(*i)