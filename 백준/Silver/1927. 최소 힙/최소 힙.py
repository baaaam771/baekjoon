import heapq, sys
input = sys.stdin.readline
hq = []

for i in range(int(input())):
    command = int(input())
    if command == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, command)