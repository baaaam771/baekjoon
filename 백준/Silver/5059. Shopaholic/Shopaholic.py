for i in range(int(input())):
    ans = 0
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mod = n % 3
    arr = arr[mod:]
    # print(arr)
    for i in range(0, len(arr), 3):
        ans += arr[i]
        # print(i)
    print(ans)