n = int(input())
arr = list(map(int, input().split()))
arr.sort()

times = []
temp = 0
for i in arr:
    temp += i
    times.append(temp)

print(sum(times))