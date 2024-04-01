n = int(input())
arr = list(map(int, input().split()))
dict = {}
for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

v = int(input())
if v not in arr:
    print(0)
else:
    print(dict[v])