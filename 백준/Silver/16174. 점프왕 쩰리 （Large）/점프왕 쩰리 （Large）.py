from collections import deque

def bfs(x, y):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    
    # 아래, 오른쪽 이동
    dx = [0, 1]
    dy = [1, 0]
    
    queue = deque([[x,y]])
    
    while queue:
        x, y = queue.popleft()
        present = graph[x][y]
        if present == -1:
            return True
        
        for i in range(2):
            # 아래, 오른쪽으로 이동
            nx = x + dx[i] * present
            ny = y + dy[i] * present
            
            # nx, ny가 범위 안이고
            if 0 <= nx < n and 0 <= ny < n:
                # 방문한 적이 없을 때
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])

if bfs(0,0):
    print('HaruHaru')
else: print('Hing')