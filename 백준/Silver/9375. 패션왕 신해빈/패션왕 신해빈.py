import sys
from functools import reduce
input = sys.stdin.readline

for i in range(int(input())):
    closet = {}
    for j in range(int(input())):
        a, b = input().split()
        if b in closet:
            closet[b].append(a)
        else:
            closet[b] = [a]

    cal = [len(closet[i])+1 for i in closet]
    print(reduce(lambda x, y : x * y, cal)-1 if len(cal) != 0 else 0)