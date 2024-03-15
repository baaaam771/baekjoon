n = int(input())
arr = []
ans = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

# print(arr)


for i in range(n):
    cnt = 0
    for j in arr:
        if j[0] > arr[i][0] and j[1] >arr[i][1]:
            cnt +=1 
    ans.append(cnt+1)

print(' '.join(map(str, ans)))