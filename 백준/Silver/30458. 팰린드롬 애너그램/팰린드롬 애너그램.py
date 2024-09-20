n = int(input())
arr = list(input())
# print(arr)
if n % 2 == 1:
    del arr[n // 2]
# print(arr)

alp_dict = {}
for i in arr:
    if i in alp_dict:
        alp_dict[i] += 1
    else:
        alp_dict[i] = 1

for i in alp_dict.values():
    # print(i)
    if i % 2 == 1:
        print('No')
        exit(0)
print('Yes')