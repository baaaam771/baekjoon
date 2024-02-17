while True:
    n = input()
    if n == '0':
        break
    else:
        ans = True
        num = list(map(int, n))
        for i in range(len(num)//2):
            if num[i] != num[len(num)-i-1]:
                ans = False
                print('no')
                break
        if ans == True:
            print('yes')