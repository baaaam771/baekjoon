from itertools import combinations
arr = [int(input()) for _ in range(9)]
arr.sort()

for i in combinations(arr, 7):
    if sum(list(i)) == 100:
        print(*i, sep = "\n")
        break