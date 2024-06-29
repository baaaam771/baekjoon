n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = []
for i in range(1, n+1):
    dp.append([0]*i)
dp[0][0] = arr[0][0]

for i in range(n-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + arr[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + arr[i+1][j+1])
print(max(dp[n-1]))