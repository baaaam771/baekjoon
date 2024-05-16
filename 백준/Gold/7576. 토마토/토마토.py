from collections import *
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
day = [[0] * m for _ in range(n)]
chk = [[0] * m for _ in range(n)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and day[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    day[nx][ny] = day[x][y] + 1
                    chk[nx][ny] = 1
                    q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])
            chk[i][j] = 1
        elif arr[i][j] == -1:
            chk[i][j] = 1

bfs()
# print(day)
# print(chk)

for r in chk:
    if 0 in r:
        print(-1)
        exit(0)

# print(max(day))
print(max(max(r) for r in day))
