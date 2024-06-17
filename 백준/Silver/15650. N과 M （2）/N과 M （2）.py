import itertools
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
for i in itertools.combinations(arr, m):
    print(' '.join(map(str, list(i))))