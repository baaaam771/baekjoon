import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))
cost = 0
for i in range(m-1):
    cost += dp[num[i]-1][num[i+1]-1]
print(cost)