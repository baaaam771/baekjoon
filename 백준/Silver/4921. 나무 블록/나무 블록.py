cnt = 0  # 몇 번째 케이스인가
preBlock = [0, 0]  # 이전 블럭의 좌, 우 상태를 나타낸 값
# preBlock[0]: 좌측, preBlock[1]: 우측

def input_blocks():
    global cnt
    while True:
        in_str = input().strip()
        if in_str == '0':
            break

        size = len(in_str)
        cnt += 1
        possible = True

        if in_str[0] == '1' and in_str[-1] == '2':  # 블럭 조합의 처음과 끝이 1번과 2번이어야 정상
            for i in range(size):  # 블럭 조합의 처음부터 끝까지 탐색
                left, right = find_block_key(in_str[i])  # 현재 블럭의 좌우 상태를 정수로 변환
                if i == 0:  # 첫 회에는 이전 블럭 세팅만 하고 넘어간다.
                    set_prev_block(left, right)
                else:  # 첫 회 이후에는 이전 블럭과 현재 블럭을 비교하여 가능한지 확인
                    if not check_block(left, right):  # 불가능할 시 불가능함을 출력
                        print(f"{cnt}. NOT")
                        possible = False
                        break
        else:  # 블럭 조합의 처음과 끝이 비정상인 경우 바로 종료
            print(f"{cnt}. NOT")
            possible = False

        # 위 과정에서 걸러지지 않은 경우 가능한 조합임을 출력
        if possible:
            print(f"{cnt}. VALID")

def find_block_key(b):
    if b == '1':
        return 0, 3  # 반듯, 오목 사각형
    elif b == '2':
        return 3, 0  # 오목 사각형, 반듯
    elif b == '3':
        return 3, 3  # 오목 사각형, 오목 사각형
    elif b == '4':
        return 1, 1  # 볼록 사각형, 볼록 사각형
    elif b == '5':
        return 1, 4  # 볼록 사각형, 오목 원형
    elif b == '6':
        return 4, 1  # 오목 원형, 볼록 사각형
    elif b == '7':
        return 4, 4  # 오목 원형, 오목 원형
    elif b == '8':
        return 2, 2  # 볼록 원형, 볼록 원형

def set_prev_block(left, right):
    global preBlock
    preBlock[0] = left
    preBlock[1] = right

def check_block(left, right):
    global preBlock
    preBlockRight = preBlock[1]
    nowBlockLeft = left

    possible = False
    if ((preBlockRight == 1 and nowBlockLeft == 3) or
        (preBlockRight == 3 and nowBlockLeft == 1) or 
        (preBlockRight == 2 and nowBlockLeft == 4) or 
        (preBlockRight == 4 and nowBlockLeft == 2)):
        possible = True

    set_prev_block(left, right)
    return possible

# 실행
input_blocks()
