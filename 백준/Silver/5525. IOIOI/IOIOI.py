n = int(input())
p = 'IO'*n+'I'
# print(P)
m = int(input())
s = input()
arr = []
for i in range(0, m+1-len(p)):
    arr.append(s[i:i+len(p)])
# print(arr)
print(arr.count(p))