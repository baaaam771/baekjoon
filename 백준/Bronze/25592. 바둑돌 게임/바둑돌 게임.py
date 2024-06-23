n = int(input())
cnt = 0

for i in range(100000):
    temp = cnt
    cnt += i
    if i % 2 == 1 and cnt >= n:
        break

if n < temp:
    print(0)
else:
    print(cnt-n)
