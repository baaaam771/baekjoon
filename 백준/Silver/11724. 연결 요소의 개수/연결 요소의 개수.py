import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
n, m =  map(int,input().split())

graph = [[0]*n for _ in range(n)]
visited = [False]*n

for i in range(m):
    a, b =  map(int,input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = 1

def dfs(v):
    for i in range(n):
        if graph[v][i] and not visited[i]:
            visited[i] = True
            dfs(i)


chk = 0
for i in range(n):
    if not visited[i]:
        chk += 1
        dfs(i)

print(chk)