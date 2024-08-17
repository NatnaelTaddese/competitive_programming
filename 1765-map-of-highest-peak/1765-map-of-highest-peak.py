class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        m, n = len(isWater), len(isWater[0])
        max_height = 0
        heights = [[-1 for _ in range(n)] for _ in range(m)]
        # -1 if not visited
        # visited = set()
        def inBound(i,j):
            return 0 <= i < m and 0 <= j < n
        queue = deque()


        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    # bfs(self, i,j)
                    heights[i][j] = 0
                    queue.append((i,j))
        
        #BFS
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if inBound(x,y) and heights[x][y] == -1:
                    # not seen
                    heights[x][y] = heights[i][j] + 1
                    queue.append((x,y))
        
        return heights