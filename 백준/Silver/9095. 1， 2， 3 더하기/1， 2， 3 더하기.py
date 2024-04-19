n = int(input())
arr = [int(input()) for i in range(n)]
ans = [0, 1, 2, 4]
for i in range(4, 12):
    ans.append(ans[i-1] + ans[i-2] + ans[i-3])
for i in arr:
    print(ans[i])