n, m = map(int, input().split())
A = []

for _ in range(n):
    A.append(list(map(int, input().split())))

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        A[i][j] += arr[j]
    print(' '.join(map(str, A[i])))