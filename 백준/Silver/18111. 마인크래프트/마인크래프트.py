n, m, b = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# print(arr)
d = {}
for line in arr:
    for i in range(m):
        if line[i] in d:
            d[line[i]] += 1
        else:
            d[line[i]] = 1


sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

ans = {}
flag = False
# std = k[0]
for std in sorted_dict.keys():
    while flag == False:
        # print(std)
        add = 0
        sub = 0
        # for line in arr:
        #     for i in range(m):
        for h, cnt in sorted_dict.items():
            if h > std:
                sub += (h - std) * cnt
                # print(f'sub {sub}')
            elif h < std:
                add += (std - h) * cnt
                # print(f'add {add}')
        # print(f'sub {sub} add {add}')
        if sub + b < add:
            std -= 1
        else :
            ans1 = std
            ans2 = add + 2*sub
            ans[ans1] = ans2
            flag == True
            break
# print(ans)

value = min(ans.values())
key = [i for i in ans.keys() if ans[i] == value]
key.sort()
# print(f'key {key} value {value}')


# print(str(ans2)+' '+str(ans1))
print(str(value)+' '+str(key[-1]))         