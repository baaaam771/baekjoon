import sys
input = sys.stdin.readline
a, n = map(int, input().split())
num = [i for i in range(1, a+1)]
ans = []
p = 0
while len(num)!=0:
    p = p+n-1
    if p>=len(num):
        p = p%len(num)
    ans.append(num[p])
    num.remove(num[p])
list = ', '.join(map(str, ans))
print(f'<{list}>')