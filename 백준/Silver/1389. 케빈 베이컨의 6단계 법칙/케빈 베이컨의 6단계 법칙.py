from collections import*

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# cnt_arr = [0] * (n+1)

# print(graph)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

temp_bacon = []
final_bacon = []

def bfs(start):
    visited = [0] * (n+1)
    cnt_arr = [0] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        p = q.popleft()
        temp_list = graph[p]
        for i in temp_list:
            if visited[i] == 0:
                cnt_arr[i] = cnt_arr[p] + 1
                visited[i] = 1
                q.append(i)
    return cnt_arr
                
for i in range(1, n+1):
        t_arr = bfs(i)
        temp_bacon.append(sum(t_arr))


# print(temp_bacon)

min = 10**6
ans = 0
for i in range(n):
    if temp_bacon[i] < min:
        min = temp_bacon[i]
        ans = i+1

print(ans)