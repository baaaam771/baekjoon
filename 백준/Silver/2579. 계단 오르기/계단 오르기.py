import sys
input = sys.stdin.readline
n = int(input())
point = [0]
for i in range(n):
    point.append(int(input()))
# point = [int(input()) for i in range(n)]
# print(point)

if n == 1:
    print(point[1])
elif n == 2:
    print(point[1] + point[2])
else:
    dp = [0]
    dp.append(point[1])
    dp.append(sum(point[1:3]))
    # print(dp)
    for i in range(3, n+1):
        dp.append(max(dp[i-2]+point[i], dp[i-3]+point[i]+point[i-1]))
    print(dp[-1])