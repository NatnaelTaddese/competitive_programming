class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_valid(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True

        def backtrack(row):
            if row == n:
                solution = [''.join(row) for row in board]
                solutions.append(solution)
                return
            
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        solutions = []
        board = [['.'] * n for _ in range(n)]

        backtrack(0)
        return solutions