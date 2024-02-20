import sys
input = sys.stdin.readline
stack = []
for i in range(int(input())):
    a = list(input().split())
    if a[0] == 'push':
        stack.append(int(a[1]))
    elif a[0] == 'pop':
        print(stack.pop(-1) if len(stack) != 0 else -1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif a[0] == 'top':
        print(stack[-1] if len(stack) != 0 else -1)