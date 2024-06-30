n = int(input())
num = 0
i = 0
while num < n :
    num += i
    i += 1
if num == n :
    print(i-1)
else:
    print(i-2)