good = [1,1,2,2,2,8]
get = list(map(int, input().split()))
ans = []
for i in range(6):
    ans.append(good[i]-get[i])
print(' '.join(map(str, ans)))