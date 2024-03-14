import sys
input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for i in range(k)]
# print(sum(arr))
# arr.sort()

def cut(num):
    cnt = 0
    for i in arr:
        cnt += i // num
    return cnt

# print(cut(200))

def binary_search(arr, target):
    start = 0
    end = max(arr)
    while start <= end:
        # print(f'{start}, {end}')
        mid = (start + end) // 2
        if mid == 0:
            return(1)
        # print(mid)
        # print(cut(mid))
        if cut(mid) >= target:
            start = mid +1
        else:
            end = mid - 1
        # print(f'ans {start} {end}')
    return end

print(binary_search(arr, n))