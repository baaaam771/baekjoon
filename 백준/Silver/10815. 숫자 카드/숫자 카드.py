import sys
input = sys.stdin.readline
n = int(input())
myCard = list(map(int, input().split()))
m = int((input()))
mCard = list(map(int, input().split()))
answer = [0]*m

dict = {v: k for k, v in enumerate(mCard)}
# print(dict)

for i in myCard:
    if i in dict:
        answer[dict[i]]=1

print(' '.join(str(i) for i in answer))