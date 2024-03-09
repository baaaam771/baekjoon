stk = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        stk.pop()
    else:
        stk.append(n)
print(sum(stk))