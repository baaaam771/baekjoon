a, b = map(int, input().split())

mul = 1
div =1

for i in range(a, a-b, -1):
    mul *= i

for i in range(b, 1, -1):
    div *= i

print(mul//div)