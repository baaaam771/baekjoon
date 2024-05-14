n, k = map(int, input().split())
if n >= k:
    print(n-k)
    exit(0)
dp = [0] * (k+1)
for i in range(n):
    dp[n-i] = i

for i in range(n+1, k+1):
    if i % 2 == 0:
        dp[i] = min(dp[i-1]+1, dp[i//2]+1)
    else:
        dp[i] = min(dp[i-1]+1, dp[(i+1)//2]+2)
# print(dp)
print(dp[k])