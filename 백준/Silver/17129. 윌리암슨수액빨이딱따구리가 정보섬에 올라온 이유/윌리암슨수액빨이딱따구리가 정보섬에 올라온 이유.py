from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n,m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append((i, j, 0))
            graph[i][j] = 1
           
while queue:
    x, y, d = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
            if graph[nx][ny] in [3,4,5]:
                print('TAK')
                print(d + 1)
                exit()

            queue.append((nx, ny, d + 1))
            graph[nx][ny] = 1
print('NIE')