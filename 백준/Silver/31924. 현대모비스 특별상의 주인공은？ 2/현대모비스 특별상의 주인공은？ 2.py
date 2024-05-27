n = int(input())
arr = [list(input()) for _ in range(n)]
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
# print(arr)

letter = ['M', 'O', 'B', 'I', 'S']

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'M':
            for k in range(8):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx <n and 0 <= ny <n:
                    if arr[nx][ny] == 'O':
                        nx += dx[k]
                        ny += dy[k]
                        if 0 <= nx <n and 0 <= ny <n:
                            if arr[nx][ny] == 'B':
                                nx += dx[k]
                                ny += dy[k]
                                if 0 <= nx <n and 0 <= ny <n:
                                    if arr[nx][ny] == 'I':
                                        nx += dx[k]
                                        ny += dy[k]
                                        if 0 <= nx <n and 0 <= ny <n:
                                            if arr[nx][ny] == 'S':
                                                cnt += 1

print(cnt)