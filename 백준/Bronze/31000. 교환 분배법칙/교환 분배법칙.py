n = int(input())
cnt = 0

for a in range(-n, n + 1):
    if a == 0:
        cnt += (2 * n + 1) ** 2
    else:
        target = 1 - a
        b_min = max(-n, target - n)
        b_max = min(n, target + n)
        cnt += b_max - b_min + 1

print(cnt)
