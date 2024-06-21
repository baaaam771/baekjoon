n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

nums = []
def back(dep, point):
    if dep == m:
        print(*nums)
        return
    for i in range(point, len(arr)):
        nums.append(arr[i])
        back(dep+1, i)
        nums.pop()
back(0, 0)