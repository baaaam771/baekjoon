import sys
input = sys.stdin.readline

L, R, A = map(int, input().rstrip().split())
a, b = min(L, R), max(L, R)
t = min(A, b-a)
a += t
A -= t
res = a*2 + (A//2*2 if A else 0)
print(res)