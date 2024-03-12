import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
# print(arr)
arr.sort()

dict = {}
for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
m = [k for k, v in dict.items() if v == max(dict.values())]
m.sort()

def my_round(num):
    if num < 0:
        return -my_round(-num)
    
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

print(my_round(sum(arr)/n))
print(arr[n//2])
print(m[0] if len(m) == 1 else m[1])
print(arr[-1]-arr[0])