import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key = lambda x : (x[1], x[0]))
# print(arr)

std = arr[0][1]
ans = 1
for i in range(1, len(arr)):
    if arr[i][0] >= std:
        ans += 1
        std = arr[i][1]

print(ans)