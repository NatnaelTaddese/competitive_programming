class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        result = []

        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(matrix[j][i])
            
            result.append(row)
                
        
        return result
            
        