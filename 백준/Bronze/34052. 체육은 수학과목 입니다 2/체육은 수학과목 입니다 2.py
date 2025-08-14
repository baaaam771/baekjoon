total = 300
for i in range(4):
    total += int(input())

if 1800 - total < 0:
    print("No")
else: print("Yes")