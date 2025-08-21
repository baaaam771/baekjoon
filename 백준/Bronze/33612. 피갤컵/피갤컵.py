Y = 2024
M = 1

N = int(input())

A = (N * 7 + M) // 12
B = (N * 7 + M) % 12

if B == 0 :
    A -= 1
    B = 12
print(Y + A, B)