arr = list(input())
ans = []
for i in arr:
    if i.isupper():
        ans.append(i.lower())
    else:
        ans.append(i.upper())
print(''.join(ans))