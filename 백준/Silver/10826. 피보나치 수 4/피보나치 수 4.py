n = int(input())

arr = [0, 1]
if n == 0:
    print(0)
    exit(0)
if n == 1:
    print(1)
    exit(0)
for i in range(2, n+1):
    arr.append(arr[i-2] + arr[i-1])
print(arr[-1])