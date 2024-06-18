import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
# chk = [0] * n
arr = []

def dfs(dep, point):
    if dep == m:
        print(*arr)
        return
    for i in range(point, n+1):
        if len(arr) == 0:
            arr.append(i)
            dfs(dep+1, i)
            arr.pop()
        else:
            if arr[-1] <= i:
                arr.append(i)
                dfs(dep+1, i)
                arr.pop()

dfs(0, 1)