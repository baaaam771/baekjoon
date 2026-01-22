from itertools import combinations as com

arr = []
for _ in range(9):
    arr.append(int(input()))

arr.sort()

for i in com(arr, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break
