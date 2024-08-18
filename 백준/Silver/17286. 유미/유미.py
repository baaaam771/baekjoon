import math
import itertools

# 유미의 위치 입력
x, y = map(int, input().split())

# 세 사람의 위치 입력
dot = []
for _ in range(3):
    dot.append(list(map(int, input().split())))

# 유미에서 각 사람까지의 거리 계산 함수
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 세 사람에게 가는 경로의 모든 순열 생성
permutations = list(itertools.permutations([0, 1, 2]))

# 최단 거리 초기화
min_distance = float('inf')

# 각 순열에 대해 최단 거리 계산
for perm in permutations:
    dist = 0
    dist += distance(x, y, dot[perm[0]][0], dot[perm[0]][1])
    dist += distance(dot[perm[0]][0], dot[perm[0]][1], dot[perm[1]][0], dot[perm[1]][1])
    dist += distance(dot[perm[1]][0], dot[perm[1]][1], dot[perm[2]][0], dot[perm[2]][1])
    
    # 최단 거리 갱신
    if dist < min_distance:
        min_distance = dist

# 결과 출력 (소수점 이하 버림)
print(math.floor(min_distance))
