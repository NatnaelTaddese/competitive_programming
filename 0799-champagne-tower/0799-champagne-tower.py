class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0] * k for k in range(1, query_row + 2)]
        
        dp[0][0] = poured
        
        for row in range(query_row):
            for col in range(row + 1):
                if dp[row][col] > 1:
                    overflow = (dp[row][col] - 1) / 2.0
                    dp[row + 1][col] += overflow
                    dp[row + 1][col + 1] += overflow
                    dp[row][col] = 1 
        
        return min(1, dp[query_row][query_glass])