letters = list(input())
count = {}
for i in letters:
    big = i.upper()
    if big in count:
        # count['i'] = count['i']+1
        count[big] += 1
        # print(count)
    else:
        count[big] = 1
        # print(count)

# print(count)
tmp = [k for k,v in count.items() if max(count.values()) == v]
if len(tmp) == 1:
    print(tmp[0])
else:
    print("?")
