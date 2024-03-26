n, m = map(int, input().split())
A = set()
B = set()
for _ in range(n):
    A.add(input())
for _ in range(m):
    B.add(input())

ans = A & B
print(len(ans))
for i in sorted(ans):
    print(i)