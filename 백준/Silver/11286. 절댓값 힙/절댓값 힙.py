import heapq as hq
import sys

p_arr = []
n_arr = []

for i in range(int(input())):
    n = int(sys.stdin.readline())
    if n != 0:
        if n > 0:
            hq.heappush(p_arr, n)
        else:
            hq.heappush(n_arr, -n)
    else:
        if len(p_arr) == 0 and len(n_arr) > 0:
            num = hq.heappop(n_arr)
            print(-num)
        elif len(p_arr) > 0 and len(n_arr) == 0:
            print(hq.heappop(p_arr))
        elif len(p_arr) == 0 and len(n_arr) == 0:
            print(0)
        else:
            if p_arr[0] < n_arr[0]:
                print(hq.heappop(p_arr))
            elif p_arr[0] >= n_arr[0]:
                num = hq.heappop(n_arr)
                print(-num)