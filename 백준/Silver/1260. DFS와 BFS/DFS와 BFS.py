n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)

def dfs(v):
    visited_dfs[v] = 1
    print(v, end = ' ')
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited_dfs[i] == 0:
            dfs(i)
            
def bfs(v):
    queue = [v]
    visited_bfs[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(1, n + 1):
            if graph[v][i] == 1 and visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1
dfs(v)
print()
bfs(v)