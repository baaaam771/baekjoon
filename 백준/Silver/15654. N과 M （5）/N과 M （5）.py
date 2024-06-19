import itertools
n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
for s in itertools.permutations(arr, m):
    print(*s)