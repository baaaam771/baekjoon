import sys
input = sys.stdin.readline
n = int(input())
# num = [input() for _ in range(n)]
num = [int(input().rstrip()) for _ in range(n)]
num = list(set(num))
num.sort()
print('\n'.join(map(str, num)))
# for i in num:
#     print(i)