arr = []
while 1:
    try:
        n = int(input())
        if n % 2 == 1:
            arr.append(n)
    except:
        break

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
