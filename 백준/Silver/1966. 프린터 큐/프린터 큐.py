from collections import deque
# q = deque()

num = int(input())
for i in range(num):
    q = deque()
    cnt = 0
    checkBreak = False
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    lev = arr[m]
    for i in range(n):
        q.append((i, arr[i]))
    
    i = 0
    step = sorted(arr, reverse=True)
    
    k = len(q)

    while len(q) != 0:
        # print(f'step {step[i]}')
        for _ in range(k):
            if q[0][1] == step[i]:
                if q[0] == (m, lev):
                        q.popleft()
                        print(cnt+1)
                        checkBreak = True
                        break
                else:
                    q.popleft()
                    cnt += 1
                    i += 1
                    k -= 1
                    # print(f'k {k}')
                    # print(q)
            else:
                q.append(q.popleft())
                # print(f'k {k}')
                # print(q)
        if checkBreak == True:
            break