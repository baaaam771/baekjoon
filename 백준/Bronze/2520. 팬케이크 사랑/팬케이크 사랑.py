# 팬케이크 반죽을 만들기 위해 필요한 재료 비율
std_ing = [0.5, 0.5, 0.25, 0.0625, 0.5625]  # 우유, 계란 노른자, 설탕, 소금, 밀가루
# 팬케이크 종류별로 필요한 토핑 비율
std_top = [1, 30, 25, 10]  # 바나나, 딸기잼, 초콜릿 스프레드, 호두

t = int(input())  # 테스트 케이스의 개수

for _ in range(t):
    _ = input()  # 빈 줄
    ing = list(map(int, input().split()))  # 우유, 계란 노른자, 설탕, 소금, 밀가루
    top = list(map(int, input().split()))  # 바나나, 딸기잼, 초콜릿 스프레드, 호두

    # 각 재료로 만들 수 있는 최대 반죽 개수를 계산
    max_dough = float('inf')
    for i in range(5):
        max_dough = min(max_dough, ing[i] // std_ing[i])

    # 각 토핑으로 만들 수 있는 팬케이크 개수를 계산
    total_pancakes = 0
    for i in range(4):
        total_pancakes += top[i] // std_top[i]

    # 최종적으로 만들 수 있는 팬케이크의 최대 개수는 반죽과 토핑 둘 다 고려해야 함
    if max_dough < total_pancakes:
        print(int(max_dough))
    else:
        print(int(total_pancakes))
