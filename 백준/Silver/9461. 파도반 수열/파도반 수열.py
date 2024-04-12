num_list = [int(input()) for _ in range(int(input()))]
arr = [0] * 101
arr[:6] = [0,1,1,1,2,2]

for i in range(6, max(num_list)+1):
    arr[i] = arr[i-1] + arr[i-5]

ans =[arr[i] for i in num_list]
print('\n'.join(map(str, ans)))