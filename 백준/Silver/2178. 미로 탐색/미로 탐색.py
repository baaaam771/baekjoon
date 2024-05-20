from collections import *
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
way = [[0] * m for _ in range(n)]
way[0][0] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a, b):
    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and way[nx][ny] == 0:
                way[nx][ny] = way[x][y] + 1
                q.append([nx, ny])

bfs(0, 0)
# print(way)
print(way[n-1][m-1])
