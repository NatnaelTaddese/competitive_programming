class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        count = 0


        # brute force solution:
        #   go through each sub matrix and add up the values, and compare it to the target
        
        # slightly better brute force:
        #   go through the sub matrices but instead of adding up everytime, use a prefix_sum matrix
        #   as a refernce
        '''
        def submatrix_sum(matrix, x1, y1, x2, y2):
            total = 0
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    total += matrix[i][j]
            return total
    
        for x1 in range(rows):
            for y1 in range(cols):

                for x2 in range(x1, rows):
                    for y2 in range(y1, cols):

                        if submatrix_sum(matrix, x1, y1, x2, y2) == target:
                            count += 1

        return count
        '''
        #########################
        # slighty better solution

        prefix_sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum_matrix[i][j] = prefix_sum_matrix[i - 1][j] + prefix_sum_matrix[i][j - 1] - prefix_sum_matrix[i - 1][j - 1] + matrix[i - 1][j - 1]


        # we can iterate through possible rows
        # 0: 0,1,2
        # 1: 1,2
        # 2: 2
        '''
        [0,1,0]     [0,1,1]
        [1,1,1]     [1,3,4]
        [0,1,0]     [1,4,5]

        [1, -1]
        [-1, 1]
        '''
        for row1 in range(1, rows + 1):
            for row2 in range(row1, rows + 1):
                prefix_sum = {}

                for col in range(1, cols + 1):
                    current_sum = prefix_sum_matrix[row2][col] - prefix_sum_matrix[row1 - 1][col]

                    if current_sum == target:
                        count += 1

                    count += prefix_sum.get(current_sum - target, 0)

                    prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count