n, m = map(int, input().split())

check1 = [[0] * m for _ in range(n)]
check2 = [[0] * m for _ in range(n)]
cnt1 = 0
cnt2 = 0 
arr = []

for i in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            if arr[i][j] == 'W':
                check1[i][j] = 1
                cnt1 += 1
        else:
            if arr[i][j] == 'B':
                check1[i][j] = 1
                cnt1 += 1

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            if arr[i][j] == 'B':
                check2[i][j] = 1
                cnt2 += 1
        else:
            if arr[i][j] == 'W':
                check2[i][j] = 1
                cnt2 += 1

grp = [check1, check2]

min = 64
v = 0
for group in grp:
    for i in range(n-7):
        for j in range(m-7):
            for a in range(8):
                v += sum(group[i+a][j:j+8])
            if v < min:
                min = v
                v = 0
            else:
                v = 0

print(min)