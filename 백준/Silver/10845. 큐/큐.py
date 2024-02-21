import sys
from collections import deque
input = sys.stdin.readline
q = deque() 
for _ in range(int(input())):
    command = input().rstrip()
    if command == 'pop':
        print(q.popleft() if q else -1)
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        print(0 if q else 1)
    elif command == 'front':
        print(q[0] if q else -1)
    elif command == 'back':
        print(q[-1] if q else -1)
    else:
        _, n = command.split()
        q.append(n)