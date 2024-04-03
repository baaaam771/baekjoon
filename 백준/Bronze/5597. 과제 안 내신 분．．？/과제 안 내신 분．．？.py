arr = set([i for i in range(1, 31)])
check = set([int(input()) for i in range(28)])
print('\n'.join(map(str, sorted(list(arr-check)))))