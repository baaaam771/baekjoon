n, m = map(int, input().split())
arr = list(map(int, input().split()))

def cut(arr, target):
    cnt = 0
    for i in arr:
        if i > target:
            cnt += i-target
    return cnt

# arr.sort()
# start = arr[0]
# end = arr[-1]

def bisect(start, end, target):
    ans = 0
    while start <= end:
        mid = (start+end)//2
        # print(start, end, mid)
        get = cut(arr, mid)
        if get < target:
            end = mid - 1
        else:
            start = mid + 1
            ans = mid
    return ans

print(bisect(1, max(arr), m))