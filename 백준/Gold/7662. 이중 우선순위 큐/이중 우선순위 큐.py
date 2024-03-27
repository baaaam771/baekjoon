import heapq, sys
input = sys.stdin.readline

for _ in range(int(input())):
    min_hq = []
    max_hq = []
    num_set = set()
    for i in range(int(input())):
        a, b = input().split()
        if a == 'I':
            heapq.heappush(min_hq, (int(b), i))
            heapq.heappush(max_hq, (-int(b), i))
            num_set.add(i)
        else:
            if int(b) == -1: 
                while min_hq and min_hq[0][1] not in num_set:
                    heapq.heappop(min_hq)
                if min_hq:
                    ele = heapq.heappop(min_hq) 
                    num_set.remove(ele[1])
            else:
                while max_hq and max_hq[0][1] not in num_set:
                    heapq.heappop(max_hq)
                if max_hq:
                    ele = heapq.heappop(max_hq) 
                    num_set.remove(ele[1])
        # print(min_hq, max_hq, num_set)
    
    while min_hq and min_hq[0][1] not in num_set:
        heapq.heappop(min_hq)
    while max_hq and max_hq[0][1] not in num_set:
        heapq.heappop(max_hq)

    if min_hq and max_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print('EMPTY')

