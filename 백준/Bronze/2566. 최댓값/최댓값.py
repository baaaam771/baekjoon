row = 0
col = 0
top = 0
for i in range(9):
    line = list(map(int, input().split()))
    v = max(line)
    if v > top:
        top = v
        row = i
        col = line.index(v)
    # print(f'row: {row}, col: {col}, top: {top}')
print(top)
print(row+1, col+1)