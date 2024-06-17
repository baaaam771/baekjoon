n = int(input())
std = []
for _ in range(n):
    std.append(sorted(list(map(int, input().split()))))
std.sort(key=lambda box: box[0] * box[1] * box[2])

m = int(input())
for _ in range(m):
    temp = sorted(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        if std[i][0] >= temp[0] and std[i][1] >= temp[1] and std[i][2] >= temp[2]:
            print(std[i][0] * std[i][1] * std[i][2])
            break
        else:
            cnt += 1
    if cnt == n:
        print('Item does not fit.')