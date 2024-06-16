import sys
input = sys.stdin.readline
n, q = map(int, input().split())

# 모든 컴퓨터의 초기 상태는 감염되지 않음 (0)
infected = [0] * (n + 1)
# 초기 감염되지 않은 컴퓨터의 수
uninfected_count = n

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        if infected[x] == 0:
            infected[x] = 1
            uninfected_count -= 1
    elif query[0] == 2:
        x = query[1]
        if infected[x] == 1:
            infected[x] = 0
            uninfected_count += 1
    elif query[0] == 3:
        print(uninfected_count)
