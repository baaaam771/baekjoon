arr = input().split('-')
# print(arr)
for i, ele in enumerate(arr):
    if '+' in ele:
        # print(i, ele)
        arr[i] = sum(map(int, ele.split('+')))
        # print(arr)
    else:
        arr[i] = int(ele)
        # print(arr)

if len(arr) <= 1:
    print(arr[0])
else:
    cnt = arr[0]
    for i in range(1, len(arr)):
        cnt -= arr[i]
    print(cnt)