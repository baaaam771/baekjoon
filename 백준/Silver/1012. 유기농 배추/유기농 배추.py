import sys
sys.setrecursionlimit(10 ** 6)
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0    
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)