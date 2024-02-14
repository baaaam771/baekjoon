list = []
for i in range(int(input())):
    x, y = map(int, input().split())
    list.append((y, x))
   
list.sort()
for i in list:
    print(i[1], i[0])