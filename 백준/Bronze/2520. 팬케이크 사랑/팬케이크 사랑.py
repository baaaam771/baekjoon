std_ing = [0.5, 0.5, 0.25, 0.0625, 0.5625]
std_top = [1, 30, 25, 10 ]
t = int(input())
for _ in range(t):
    _ = input()
    ing = list(map(int, input().split()))
    top = list(map(int, input().split()))
    min_ing = float('inf')
    for i in range(5):
        temp = ing[i] // std_ing[i]
        if temp < min_ing:
            min_ing = temp
    total_top = 0
    for i in range(4):
        temp = top[i] // std_top[i]
        total_top += temp
    if min_ing <= total_top:
        print(int(min_ing))
    else:
        print(int(total_top))