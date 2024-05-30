from collections import *
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

graph = [[] for _ in range(n)]

# print(graph)
# print(arr)

for index, row in enumerate(arr):
    for i in range(n):
        if row[i] == 1:
            graph[index].append(i)

# print(graph)

def bfs(point):
    visited = [0] * n
    q = deque()
    q.append(point)
    while q:
        p = q.popleft()
        temp_list = graph[p]
        for i in temp_list:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return visited

# print(bfs(0))

ans_graph = []
for i in range(n):
    ans_graph.append(' '.join(map(str, bfs(i))))

# print(ans_graph)
for i in ans_graph:
    print(i)
