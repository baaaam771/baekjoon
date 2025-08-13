while 1:
    try:
        n = int(input())
    except:
        break

    a = 0
    num = 0    
    while 1:
        num += 10 ** a
        if num % n == 0:
            print(a + 1)
            break
        else:
            a += 1