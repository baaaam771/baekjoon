from collections import deque
m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
day = [[[0] * m for _ in range(n)] for _ in range(h)]
chk = [[[0] * m for _ in range(n)] for _ in range(h)]

# print(arr)

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        z, y, x = q.popleft()
        # print(z,y,x)
        chk[z][y][x] = 1
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            # print(nz, ny, nx)
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and chk[nz][ny][nx] == 0:
                # print(arr[nz][ny][nx])
                if arr[nz][ny][nx] == 0:
                    q.append([nz, ny, nx])
                    day[nz][ny][nx] = day[z][y][x] + 1
                    chk[nz][ny][nx] = 1

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i, j, k])
            if arr[i][j][k] == -1:
                chk[i][j][k] = 1

bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if chk[i][j][k] == 0:
                print(-1)
                exit(0)

top = 0
for i in day:
    for j in i:
        temp = max(j)
        if temp > top:
            top = temp

print(top)
