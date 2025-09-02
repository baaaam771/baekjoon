N = int(input())

cnt = 0
std = 1
while N > 0:
    if N >= std:
        N -= std
        std += 1
        cnt += 1
    else:
        std = 1

print(cnt)