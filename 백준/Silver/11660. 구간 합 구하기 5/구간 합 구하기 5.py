import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
# print(arr)
sum_arr = []
zero_list = [0] * (n + 1)
sum_arr.append(zero_list)


for i in range(1, n+1):
    temp_list = [0]
    temp = 0
    for j in range(n):
        temp += arr[i-1][j]
        temp_list.append(sum_arr[i-1][j+1] + temp)
    sum_arr.append(temp_list)

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1])

