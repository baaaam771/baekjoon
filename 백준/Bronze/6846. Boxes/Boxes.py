import itertools

# 입력을 받습니다.
n = int(input())
std_boxes = [sorted(list(map(int, input().split()))) for _ in range(n)]
m = int(input())
items = [list(map(int, input().split())) for _ in range(m)]

# 가능한 모든 회전 형태를 생성하는 함수
def get_rotations(item):
    return set(itertools.permutations(item))

# 각 아이템에 대해 적합한 박스를 찾고 결과를 출력합니다.
for item in items:
    item_rotations = get_rotations(item)
    min_volume = float('inf')
    fits = False
    for box in std_boxes:
        for rotation in item_rotations:
            if all(rotation[i] <= box[i] for i in range(3)):
                fits = True
                min_volume = min(min_volume, box[0] * box[1] * box[2])
    if fits:
        print(min_volume)
    else:
        print("Item does not fit.")
