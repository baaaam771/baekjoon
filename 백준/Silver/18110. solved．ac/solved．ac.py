import sys
input = sys.stdin.readline
def Round(num):
    if num - int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
    exit(0)
arr = [int(input()) for _ in range(n)]
arr.sort()
# print(arr)

k = Round(n*0.15)
if k > 0:
    del arr[:k]
    del arr[-k:]
    print(Round(sum(arr)/len(arr)))
else:
    print(Round(sum(arr)/len(arr)))