n, l = map(int, input().split())
# print(n, l)
hole = list(map(int, input().split()))

tape=1

hole.sort()

point = hole[0]
for i in range(1, n):
    # print(i, "i")
    if hole[i] in range(point, point+l):
        # print(point)
        continue
    else:
        tape += 1
        point = hole[i]
        # print(point)

print(tape)
