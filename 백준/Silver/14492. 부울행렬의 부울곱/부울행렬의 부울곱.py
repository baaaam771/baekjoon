n = int(input())
A = []
B = []
C = [[0]*n for i in range(n)]
for i in range(n):
    A.append(list(map(int, input().split())))
for i in range(n):
    B.append(list(map(int, input().split())))
# print(A)
# print(B)
# print(C)
for i in range(n):
    for j in range(n):
        temp = []
        for k in range(n):
            temp.append(A[i][k] * B[k][j])
        # print(temp)
        if 1 in temp:
            C[i][j] = 1
# print(C)
# for i in range(n):
    # print(*C[i])
    # print(' '.join(map(str, C[i])))
temp_sum = 0
for i in range(n):
    temp_sum += sum(C[i])
print(temp_sum)
