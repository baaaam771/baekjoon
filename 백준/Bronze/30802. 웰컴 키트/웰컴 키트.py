n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
a = 0
for i in size:
    if i % t:
        a += i // t + 1
    else:
        a += i // t
print(a)
print(sum(size) // p, sum(size)% p)