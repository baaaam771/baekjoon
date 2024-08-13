import sys
input = sys.stdin.readline

#입력
N = int(input())
lst = list(map(int, input().split()))

#홀수, 짝수합
odd_sum = 0
even_sum = 0
for i in range(N):
    if i%2 == 0:
        odd_sum += lst[i]
    else:
        even_sum += lst[i]

# N=3이고 홀수합이 더 많다면 불가능
if N == 3 and odd_sum > even_sum:
    print(-1)
# 그 외에는 절대값 차이만큼 반복
else:
    print(abs(odd_sum-even_sum))