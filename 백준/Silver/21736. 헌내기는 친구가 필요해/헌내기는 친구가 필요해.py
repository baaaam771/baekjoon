from collections import*
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
chk = [[0] * m for _ in range(n)]
# print(arr)
# print(chk)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    cnt = 0
    q = deque()
    q.append([a, b])
    chk[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            # print(ix, iy)
            if 0 <= ix < n and 0 <= iy < m and chk[ix][iy] == 0:
                if arr[ix][iy] == 'O' or arr[ix][iy] == 'I':    
                    q.append([ix, iy])
                    chk[ix][iy] = 1
                elif arr[ix][iy] == 'P':
                    q.append([ix, iy])
                    chk[ix][iy] = 1
                    cnt += 1
    return cnt


for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            sx, sy = i, j
            break
# print(sx, sy)

ans = bfs(sx, sy)
print('TT' if ans == 0 else ans)
 