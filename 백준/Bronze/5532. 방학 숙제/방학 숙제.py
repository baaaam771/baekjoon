import math

arr = []
for i in range(5):
    arr.append(int(input()))
print(arr[0] - max(math.ceil(arr[1]/arr[3]), math.ceil(arr[2]/arr[4])))