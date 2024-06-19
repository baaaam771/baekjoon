n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
nums = []
chk = [0] * 10001

def back(dep, point):
    if dep == m:
        print(*nums)
        return
    
    for i in arr:
        if chk[i] == 0:
            chk[i] = 1
            nums.append(i)
            back(dep + 1, i)
            chk[i] = 0
            nums.pop()

back(0, arr[0])