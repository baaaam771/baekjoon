n, k = map(int, input().split())
if k == 1:
    print(1)
    exit(0)
cnt = 0    
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
        if cnt == k:
            print(i)
            exit(0)
if cnt != k:
    print(0)