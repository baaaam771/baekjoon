n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

temp = 0
for i in a:
    temp += i
for j in b:
    if j != 0:
        temp *= j
print(temp)