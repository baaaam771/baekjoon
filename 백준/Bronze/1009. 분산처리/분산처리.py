for _ in range(int(input())):
    a, b = map(int, input().split())
    a1 = a % 10
    if a1 == 0:
        print(10)
    elif a1 == 1 or a1 == 5 or a1 == 6:
        print(a1)
    elif a1 == 4 or a1 == 9:
        b1 = b % 2
        if b1 == 0:
            print(a1 * a1 % 10)
        else:
            print(a1)
    else:
        b1 = b % 4
        if b1 == 0:
            print(a1 ** 4 % 10)
        else:
            print(a1 ** b1 % 10)