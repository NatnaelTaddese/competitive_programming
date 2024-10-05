class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row, col = len(dungeon), len(dungeon[0])
        dp = [[1 for _ in range(col + 1)] for _ in range(row + 1)]

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                dp[i][j] = abs(min(1,dungeon[i][j])) + min(dp[i + 1][j],dp[i][j + 1])
        
        return dp[0][0]
