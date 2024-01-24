heights = []
for _ in range(9):
    heights.append(int(input()))

# print(heights)

for i in range(9):
    for j in range(i+1, 9):
        # print(i, j)
        new = heights[:]
        del new[i]
        del new[j-1]
        # print(new)
        # print(heights)
        all = sum(new)
        # print(all)
        if all == 100:
            arrange = sorted(new)
            print(*arrange, sep='\n')
            exit(0)