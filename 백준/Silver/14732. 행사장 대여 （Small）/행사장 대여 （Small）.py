arr = [[0] * 501 for _ in range(501)]
# print(arr)
n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    # print(x1, y1, x2, y2)
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

total_sum = sum(sum(sublist) for sublist in arr)
print(total_sum)