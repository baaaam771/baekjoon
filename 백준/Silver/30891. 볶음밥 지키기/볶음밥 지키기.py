import sys
import math

input = sys.stdin.read
data = input().split()

N = int(data[0])
R = int(data[1])

xList = []
yList = []

index = 2
for _ in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    xList.append(x)
    yList.append(y)
    index += 2

minX = min(xList)
maxX = max(xList)
minY = min(yList)
maxY = max(yList)

cnt = 0
resultX = 0
resultY = 0

for i in range(minX, maxX + 1):
    for j in range(minY, maxY + 1):
        tempCnt = 0
        for x, y in zip(xList, yList):
            r = math.sqrt((i - x)**2 + (j - y)**2)
            if r <= R:
                tempCnt += 1
        if cnt < tempCnt:
            cnt = tempCnt
            resultX = i
            resultY = j

print(resultX, resultY)