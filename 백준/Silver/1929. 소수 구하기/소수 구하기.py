import math
m, n = map(int, input().split())
arr = [1 for i in range(n+1)]
arr[1] = 0

for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == 1:
        a = 2  
        while i*a <= n:
            arr[i*a] = 0
            a += 1

for i in range(m, n+1):
    if arr[i] == 1:
        print(i)