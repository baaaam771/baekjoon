def mill_workpieces_optimized(W, S, X, Y, workpieces, milling_steps):
    # 각 열에 대한 절삭 단계의 최대값 계산
    max_cut = [0] * X
    for step in milling_steps:
        for i in range(X):
            max_cut[i] = max(max_cut[i], step[i])
    
    results = []
    for workpiece in workpieces:
        final_heights = [
            max(0, min(height, Y - max_cut[i])) for i, height in enumerate(workpiece)
        ]
        results.append(final_heights)
    
    return results

# 입력 데이터 받기
import sys
input = sys.stdin.read
data = input().split()

W = int(data[0])
S = int(data[1])
X = int(data[2])
Y = int(data[3])

workpieces = []
index = 4
for _ in range(W):
    workpieces.append(list(map(int, data[index:index + X])))
    index += X

milling_steps = []
for _ in range(S):
    milling_steps.append(list(map(int, data[index:index + X])))
    index += X

# 작업물 절삭
results = mill_workpieces_optimized(W, S, X, Y, workpieces, milling_steps)

# 결과 출력
for result in results:
    print(" ".join(map(str, result)))
