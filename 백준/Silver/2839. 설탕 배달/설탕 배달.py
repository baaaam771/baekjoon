init_val = {3:1, 4:-1, 5:1, 6:2, 7:-1, 8:2, 9:3, 10:2}
ans = 0
n = int(input())
if n<=10:
    print(init_val[n])
    exit(0)
else:
    m = n%5
    ans += n//5
    # print(ans)
    if m != 0:
        if m%2 == 0:
            ans += 2
        else:
            ans += 1

print(ans)    