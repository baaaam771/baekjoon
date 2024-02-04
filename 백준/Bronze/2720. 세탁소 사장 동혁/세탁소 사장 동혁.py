coin = [25, 10, 5, 1]
# result = []
for _ in range(int(input())):
    result = []
    money = int(input())
    for i in range(4):
        result.append(money // coin[i])
        money = money % coin[i]
    print(' '.join(str(x) for x in result))
