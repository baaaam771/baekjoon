n = int(input())
m = int(input())
if n == 0:
    print(0)
    exit(0)
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(v, graph, visitied):
    visitied[v] = True
    for i in graph[v]:
        if visitied[i] == False:
            dfs(i, graph, visitied)

# print(graph)
dfs(1, graph, visited)
print(visited.count(True)-1)
