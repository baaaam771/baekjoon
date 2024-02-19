n = int(input())
budget = list(map(int, input().split()))
top = int(input())
# start = min(budget)
start = 0
end = max(budget)

def sum_buget(list, line):
    total = 0
    for i in list:
        if i > line:
            total += line
        else:
            total += i
    return total

ans = 0
while(start <= end):
    mid = (start + end)//2
    all = sum_buget(budget, mid)
    if all < top:
        ans = mid
        start = mid + 1
    elif all > top:
        end = mid - 1
    else:
        ans = mid
        break
print(ans)


