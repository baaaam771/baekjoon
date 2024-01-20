import heapq, sys

pq_pos = []
pq_neg = []

n = int(input())

for _ in range(n):

    ori = int(sys.stdin.readline())
    if ori >0:
        heapq.heappush(pq_pos, ori)
        
    elif ori<0:
        heapq.heappush(pq_neg, -ori)
       

    elif ori==0:
        if len(pq_pos)>0 and len(pq_neg)>0:
            if abs(pq_pos[0])<abs(pq_neg[0]):
               
                print(heapq.heappop(pq_pos))

            else:
                print(-heapq.heappop(pq_neg))

        elif len(pq_pos)==0 and len(pq_neg)!=0:
            print(-heapq.heappop(pq_neg))

        elif len(pq_neg)==0 and len(pq_pos)!=0:

            print(heapq.heappop(pq_pos))

        else:
            print(0)



