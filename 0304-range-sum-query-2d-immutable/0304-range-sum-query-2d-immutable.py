class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        self.pref_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                self.pref_matrix[i + 1][j + 1] = self.pref_matrix[i][j + 1] + self.pref_matrix[i + 1][j] - self.pref_matrix[i][j] + matrix[i][j]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
#       return self.pref_matrix[row2 + 1][col2 + 1] - self.pref_matrix[row2 + 1][col1] - self.pref_matrix[row1][col2 + 1] + self.pref_matrix[row1][col1]

        return self.pref_matrix[row2 + 1][col2 + 1] - self.pref_matrix[row2 + 1][col1] - self.pref_matrix[row1][col2 + 1] + self.pref_matrix[row1][col1]

# # Your NumMatrix object will be instantiated and called as such:
# # obj = NumMatrix(matrix)
# # param_1 = obj.sumRegion(row1,col1,row2,col2)