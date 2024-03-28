import sys
input = sys.stdin.readline
memo = {}
n, m = map(int, input().split())
for i in range(n):
    site, pw = input().split()
    memo[site] = pw
# print(memo)
    
for i in range(m):
    print(memo[input().rstrip()])