from collections import deque


directions = [(-1,0), (1,0),(0,-1),(0,1)]

def bfs(n, m, matrix, start):
    queue = deque([start])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = True

    volume = 0

    while queue:
        x, y = queue.popleft()
        if matrix[x][y] != 0:
            volume += matrix[x][y]
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and matrix[nx][ny] != 0:
                queue.append((nx,ny))
                visited[nx][ny] = True
    
    return volume

    



for _ in range(int(input())):
    n, m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    # for _ in range(n):
    #     row = list(map(int, input().split()))
    print(bfs(n,m,matrix,(0,0)))
    

