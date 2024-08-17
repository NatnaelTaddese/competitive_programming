class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]

        # print(grid)
        '''
        [[1, 4, 5], 
         [2, 5, 1],
         [6, 2, 1]]

         [1, 4,     5  ], 
         [2, (5+2), 1+5],
         [6, (2+6), 1+6]
        '''
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]

