from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        if x == r2 and y == c2:
            return graph[x][y]
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return -1


n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

r1, c1, r2, c2 = map(int, input().split())
    
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

print(bfs(r1, c1))