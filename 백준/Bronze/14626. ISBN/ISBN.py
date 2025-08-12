arr = list(input())
sum = 0
lost = 0
mul = 0

for i in range(len(arr)):
    if arr[i] == '*':
        lost = i
    else:
        if i % 2 == 0:
            sum  += int(arr[i])
        else:
            sum += int(arr[i])*3

if lost % 2 == 0:
    mul = 1
else:
    mul = 3

for i in range(10):
    if (sum + i * mul) % 10 == 0:
        print(i)
        break