n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
# print(arr)

def get_sum(x_start, x_end, y_start, y_end, arr):
    plus = 0
    for i in range(x_start, x_end+1):
        plus += sum(arr[i][y_start:y_end+1])
    return plus

def get_point(x_start, x_end, y_start, y_end):
    x_mid = (x_start + x_end) // 2
    y_mid = (y_start + y_end) // 2
    return x_start, x_mid, x_end, y_start, y_mid, y_end

x_start, x_end, y_start, y_end = 0, n-1, 0, n-1
x_mid, y_mid = 0, 0
# std = n**2
white = 0
blue = 0

def four_batch(a, b, c, x, y, z, arr):
    arr.append([a, b, x, y])
    arr.append([a, b, y+1, z])
    arr.append([b+1, c, x, y])
    arr.append([b+1, c, y+1, z])

chk = [[x_start, x_end, y_start, y_end]]

# while n >= 1:
while chk:
    x_start, x_end, y_start, y_end = chk.pop(0)
    # print(chk)
    # print(x_start, x_end, y_start, y_end)
    temp = get_sum(x_start, x_end, y_start, y_end, arr)
    std = (x_end-x_start+1)*(y_end-y_start+1)
    if temp == std:
        blue += 1
    elif temp == 0:
        white += 1
    else:
        x_start, x_mid, x_end, y_start, y_mid, y_end = get_point(x_start, x_end, y_start, y_end)
        four_batch(x_start, x_mid, x_end, y_start, y_mid, y_end, chk)

print(white)
print(blue)