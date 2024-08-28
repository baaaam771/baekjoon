n = int(input())
ans = 0
ans += n//5
if n % 5:
    ans += 1
print(ans)