import itertools 

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input().split())

    if n > 32:
        print(0)
        continue

    min = 100
    for x in itertools.combinations(arr, 3):
        select = list(x)
        # print(select)
        temp = 0
        for i in range(4):
            if select[0][i] != select[1][i]:
                temp += 1
            if select[1][i] != select[2][i]:
                temp += 1
            if select[2][i] != select[0][i]:
                temp += 1
        if temp < min:
            min = temp
    print(min)