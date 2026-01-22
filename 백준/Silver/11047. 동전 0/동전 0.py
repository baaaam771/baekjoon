n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
ans = 0

for i in range(len(coin)-1, -1, -1):
    if k >= coin[i]:
        ans += (k // coin[i])
        k %= coin[i]

print(ans)