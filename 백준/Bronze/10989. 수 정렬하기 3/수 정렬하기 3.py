import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 10001
for i in range(n):
    arr[int(input())] += 1

for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)