for i in range(int(input())):
    a, b = input().split()
    # print(a, b)
    num_b = int(b)
    char_a = a[0]
    num_a = int(a[1])
    # print(ord(char_a), num_a, num_b)
    # (num_a-1)*8 + ord(char_a)-64
    if (ord(char_a)-64) % 2 == 0:
        if num_a % 2 == 0:
            left = 0
        else:
            left = 1
    else:
        if num_a % 2 == 0:
            left = 1
        else:
            left = 0
    
    if ((num_b - 1) // 8) % 2 == 1:
        if num_b % 2 == 0:
            right = 0
        else:
            right = 1
    else:
        if num_b % 2 == 0:
            right = 1
        else:
            right = 0
    # print(left, right)
    print('YES' if left == right else 'NO')