def fibo(n):
    if n == 0 or n == 1 or n == 2:
        pass
    else:
        for i in range(2, n):
            arr.append(arr[i]+ arr[i-1])
    return arr[n-1], arr[n]


n = int(input())
for _ in range(n):
    num = int(input())
    arr = [0, 1, 1]
    print(' '.join(map(str, list(fibo(num)))))