from collections import deque
n = int(input())
arr = [i for i in range(1, n+1)]
ans = []
q = deque([i for i in range(1, n+1)])

while q:
    ans.append(q.popleft())
    if q:
        q.append(q.popleft())
# print(q)
print(*ans)