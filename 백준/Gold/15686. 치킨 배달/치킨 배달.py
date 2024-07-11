n, m = map(int, input().split())
house = []
chicken = []

for i in range(n):
    temp = list(input().split())
    for j in range(n):
        if temp[j] == '1':
            house.append([i, j])
        elif temp[j] =='2':
            chicken.append([i, j])
visited = [False] * len(chicken)
# print(house)
# print(chicken)

min_ans = 10**6

def back(index, dep):
    global min_ans

    if dep == m:
        ans = 0
        for i in house:
            distance = 10**6 
            for j in range(len(visited)):
                if visited[j]:
                    check_num = abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1])
                    distance = min(distance,check_num)
            ans += distance
        min_ans = min(ans,min_ans)
        return
    
    for i in range(index,len(chicken)):
        if not visited[i]:
            visited[i] = True
            back(i+1,dep+1)
            visited[i]=False



back(0,0)

print(min_ans)
    