class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        islands = 0

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row,col):
            if not inbound(row, col) or grid[row][col] == "0":
                return
            if seen[row][col]:
                return
            
            seen[row][col] = True

            for r_chng, c_chng in directions:
                new_row = row + r_chng
                new_col = col + c_chng
                dfs(new_row, new_col)
        


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not seen[i][j]:
                    dfs(i, j)
                    islands += 1



        return islands
                    
        