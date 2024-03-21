from collections import deque

n , m , v = map(int, input().split())
graph = [[] for _ in range(n+1)]
# print(graph)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph.sort()
# print(graph)

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
# print(visited_dfs)

dfs_ans = []
bfs_ans = []
def dfs(v, graph, visited):
    visited[v] = True
    # print(v, end = ' ')
    dfs_ans.append(v)
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)

def bfs(v, graph, visited):
    q = deque([v])
    visited[v] = True
    while q:
        point = q.popleft()
        # print(point, end= ' ')
        bfs_ans.append(point)
        graph[point].sort()
        for i in graph[point]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(v, graph, visited_dfs)
print(' '.join(map(str, dfs_ans)))
bfs(v, graph, visited_bfs)
print(' '.join(map(str, bfs_ans)))