n = int(input())
mem = set()

for i in range(n):
    a, b = input().split()
    mem.add((int(a), i, b))

for i in sorted(mem):
    print(i[0], i[2])