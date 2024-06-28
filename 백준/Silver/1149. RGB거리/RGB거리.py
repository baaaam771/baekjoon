n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = []
dp.append(arr[0])

for i in range(1, n):
    temp = []
    temp.append(arr[i][0] + min(dp[i-1][1], dp[i-1][2]))
    temp.append(arr[i][1] + min(dp[i-1][0], dp[i-1][2]))
    temp.append(arr[i][2] + min(dp[i-1][0], dp[i-1][1]))
    dp.append(temp)
print(min(dp[-1]))

