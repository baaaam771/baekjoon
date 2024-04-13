import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split())) 
prefix = [0]
cum = 0
for i in num:
    cum += i
    prefix.append(cum)

for i in range(m):
    i, j = map(int, input().split())
    print(prefix[j]-prefix[i-1])