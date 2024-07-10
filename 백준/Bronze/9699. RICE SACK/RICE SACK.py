n = int(input())
for i in range(1, n+1):
    cnt = max(list(map(int, input().split())))
    print(f"Case #{i}: {cnt}")