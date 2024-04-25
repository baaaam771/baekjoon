from math import*
n = int(input())
arr = [0] * (n+1)
# print((sqrt(n)))

if (sqrt(n)) == floor(sqrt(n)):
    print(1)
    exit(0)
else:
    max_sqrt = floor(sqrt(n))
    for i in range(1, max_sqrt+1):
        arr[i] = 1
    for j in range(2, n+1):
        j_max_sqrt = floor(sqrt(j))
        cnt = 4
        # num = 0
        for k in range(1, j_max_sqrt+1):
            if cnt> arr[j-k**2]+1:
                cnt = arr[j-k**2]+1
        arr[j] = cnt    
                # num 

# print(arr)
print(arr[n])