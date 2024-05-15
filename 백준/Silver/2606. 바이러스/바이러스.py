pc = int(input()) 
connect = int(input()) 
graph = [[] for i in range(pc + 1)] 
visited=[0] * (pc + 1) 
for i in range(connect): 
    x, y = map(int,input().split())
    graph[x].append(y) 
    graph[y].append(x)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
dfs(1)
print(sum(visited)-1)