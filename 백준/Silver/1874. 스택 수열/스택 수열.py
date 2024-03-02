n = int(input())
ele = [i for i in range(1, n+1)]
num = [int(input()) for _ in range(n)]
stk = []
ans = []

a = 0
e = 0 

for _ in range(n*2):
    if len(stk) == 0:
        stk.append(ele[e])
        ans.append('+')
        e += 1
    elif stk[-1] == num[a]:
        stk.pop(-1)
        ans.append('-')
        a += 1
    elif num[a] < stk[-1]:
        print('NO')
        exit(0)
    else:
        stk.append(ele[e])
        ans.append('+')
        e += 1

print('\n'.join(ans))