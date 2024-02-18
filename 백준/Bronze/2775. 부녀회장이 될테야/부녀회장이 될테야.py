for i in range(int(input())):
    k = int(input())+1
    n = int(input())
    # apt = [[0] * n] * k
    apt = [[0] * n for _ in range(k)]

    for i in range(n):
        apt[0][i] = i+1

    for i in range(k):
        apt[i][0] = 1

    for i in range(1, k):
        for j in range(1, n):
            apt[i][j] = apt[i-1][j] + apt[i][j-1]
    
    # print(apt)
    print(apt[k-1][n-1])