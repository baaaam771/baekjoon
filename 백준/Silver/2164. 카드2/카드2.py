from collections import deque

n= int(input())
q = deque()
for i in range(1, n+1):
    q.append(i)

#print(q)

while len(q)>1:
    q.popleft()
    #print(q)
    if len(q)>1:
        q.append(q.popleft())
        #print(q)
    else:
        break

print(q.popleft())