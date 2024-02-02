adj =[[0]*100 for _ in range(100)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            adj[a+i][b+j] = 1

ans = 0       
for i in range(100):
    ans += adj[i].count(1)
print(ans)