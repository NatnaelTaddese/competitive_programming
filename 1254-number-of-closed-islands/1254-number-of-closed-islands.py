class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0, -1), (1,0),(-1,0)]
        row = len(grid)
        col = len(grid[0])
        islands = 0

        visited = set()

        

        def on_edge(x,y):
            if x == row - 1 or x == 0:
                return True
            if y == col - 1 or y == 0:
                return True
            
            return False

        def bfs(r, c):
            nonlocal islands
            is_closed = True

            queue = deque([(r,c)])
            visited.add((r,c))

            while queue:
                x, y = queue.popleft()
                print(x,y)

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < row and 0 <= ny < col):
                        is_closed = False
                        continue
                                        
                    if on_edge(nx,ny) and grid[nx][ny] == 0:
                        is_closed = False

                    if (nx,ny)not in visited and grid[nx][ny] == 0 :
                        queue.append((nx,ny))
                    visited.add((nx,ny))
                
            if is_closed:
                islands += 1
                return True
            return False

        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] == 0 and not on_edge(i,j):
                    print(i, ": ", j, bfs(i,j))
        

        return islands

        """
        [0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]]

        1 :  2 True  only
        1 :  5 False
        2 :  1 True  only
        3 :  8 True  only
        5 :  6 False
        6 :  1 True  only
        6 :  3 True  only
        8 :  3 False

        """