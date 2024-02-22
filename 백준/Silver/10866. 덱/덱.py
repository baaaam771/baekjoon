import sys
from collections import deque
input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
    c = list(input().rstrip().split())
    if c[0] == 'push_front':
        q.appendleft(int(c[1]))
    elif c[0] == 'push_back':
        q.append(int(c[1]))
    elif c[0] == 'pop_front':
        print(q.popleft() if q else -1)
    elif c[0] == 'pop_back':
        print(q.pop() if q else -1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        print(0 if q else 1)
    elif c[0] == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
