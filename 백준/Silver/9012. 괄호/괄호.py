for i in range(int(input())):
    arr = list(input())
    cnt = 0
    ans = 'YES'
    for i in arr:
        if i == '(':
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                ans = 'NO'

    if cnt > 0: ans = 'NO'
    print(ans)