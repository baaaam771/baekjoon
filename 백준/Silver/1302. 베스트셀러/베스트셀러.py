dict={}

n=int(input())
for _ in range(n):
    title = input()
    if title in dict:
        dict[title]+=1
        # print(dict)
    else:
        dict[title]=1
        # print(dict)


top =[k for k,v in dict.items() if max(dict.values()) == v]
# print(top)
top.sort()
print(top[0])

