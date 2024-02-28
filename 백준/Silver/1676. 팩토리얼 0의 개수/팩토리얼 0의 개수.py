import math
arr = list(str(math.factorial(int(input()))))
arr.reverse()
cnt = 0

for i in range(len(arr)):
    if int(arr[i]) == 0:
        cnt += 1
    else:
        break

print(cnt)