import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(input()) for _ in range(n)]
rg_arr = [row[:] for row in arr]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            rg_arr[i][j] = 'R'

# print(arr)
# print(rg_arr)

visited = [[0] * n for _ in range(n)]
color = ['R', 'G', 'B']
rg_color = ['R', 'B']

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(pic, p, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if pic[x][y] == p and visited[x][y] == 0:
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(pic, p, nx, ny)
        return True
    return False


cnt1 = 0
for std in color:
    for i in range(n):
        for j in range(n):
            if dfs(arr, std, i, j) == True:
                cnt1 += 1

# print(cnt1)

visited = [[0] * n for _ in range(n)]
cnt2 = 0
for std in rg_color:
    for i in range(n):
        for j in range(n):
            if dfs(rg_arr, std, i, j) == True:
                cnt2 += 1

print(cnt1, cnt2)