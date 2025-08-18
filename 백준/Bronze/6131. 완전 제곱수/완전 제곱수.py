n = int(input())
ans = 0
for i in range(1, 501):
    for j in range(1, 501):
        if j**2 - i**2 == n:
            ans += 1
        elif j**2 - i**2 > n:
            break
print(ans)