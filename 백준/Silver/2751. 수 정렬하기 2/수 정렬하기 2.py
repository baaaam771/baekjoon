import sys
input = sys.stdin.readline
n = int(input())
num = [int(input().rstrip()) for _ in range(n)]
num = list(set(num))
num.sort()
# print(''.join(num))
# print('\n'.join(num))
for i in num:
    print(i)