# 입력값
hh, mm = input().split(':')

# 키패드의 거리 계산 배열
way = [
    [0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
    [4, 0, 1, 2, 1, 2, 3, 2, 3, 4],
    [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
    [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
    [3, 1, 2, 3, 0, 1, 2, 1, 2, 3],
    [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
    [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
    [2, 2, 3, 4, 1, 2, 3, 0, 1, 2],
    [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
    [2, 4, 3, 2, 3, 2, 1, 2, 1, 0]
]

def effort(a, b):
    return way[int(a)][int(b)]

def total_effort(hh, mm):
    return (
        effort(hh[0], hh[1]) +
        effort(hh[1], mm[0]) +
        effort(mm[0], mm[1])
    )

hh = int(hh)
mm = int(mm)

min_effort = float('inf')
best_time = ""

for h in range(100):
    for m in range(100):

        if h % 24 == hh and m % 60 == mm:
            h_str = str(h).zfill(2)
            m_str = str(m).zfill(2)
            e = total_effort(h_str, m_str)
            if e < min_effort:
                min_effort = e
                best_time = f"{h_str}:{m_str}"

print(best_time)
