n = int(input())
for i in range(n):
    IsVPS = True
    chk_arr = []
    for j in input():
        if j == ")":
            if chk_arr:
                chk_arr.pop()
            else:
                IsVPS = False
        else:
            chk_arr.append(j)

    if chk_arr:
        IsVPS = False
    print("YES" if IsVPS else "NO")