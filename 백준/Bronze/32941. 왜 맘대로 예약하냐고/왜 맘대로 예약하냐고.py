T, X = map(int, input().split())
for i in range(int(input())):
    K = int(input())
    cls = list(map(int, input().split()))
    if X not in cls:
        print("NO")
        exit()
print("YES")
