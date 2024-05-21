hole = int(input())
cla = list(map(int, input().split()))
nut = int(input())
nuts = list(map(int, input().split()))
# print(cla)
dict = [0]
# map = [0] * (hole+1)
inv_cla = []

add = 0
for i in cla:
    i += add
    inv_cla.append(i)
    add += 1

# print(inv_cla)

temp = 0
for index, i in enumerate(inv_cla):
    if i > temp:
        addition = [index+1] * (i-temp)
        dict += addition
        temp = i
    if len(dict) > hole:
        break
    
# print(dict)

ans = []
for i in nuts:
    ans.append(dict[i])

# print(ans)
print(' '.join(map(str, ans)))