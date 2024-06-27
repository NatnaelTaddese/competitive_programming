class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        # Init with all the rotten oranges
        # also count the fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes_passed = -1

        if fresh_oranges == 0:
            return 0
        
        # BFS 
        while queue:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_oranges -= 1
        
        return minutes_passed if fresh_oranges == 0 else -1