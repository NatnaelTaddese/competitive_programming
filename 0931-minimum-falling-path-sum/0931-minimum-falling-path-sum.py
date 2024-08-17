class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)

        for row in range(n - 2, -1, -1):
            for col in range(n - 1, -1, -1):
                path = matrix[row + 1][col]

                if col > 0:
                    path = min(path, matrix[row + 1][col - 1])
                if col < n - 1:
                    path = min(path, matrix[row + 1][col + 1])

                matrix[row][col] += path
        
        return min(matrix[0])
        