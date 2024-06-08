class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        """
        [".Q..",
         "...Q",
         "Q...",
         "..Q."]

        """

    

        board = [['.'] * n for _ in range(n)]
        result = []

        def helper(row, col):
            if "Q" in board[row]:
                return False
            
            for i in range(n):
                if board[i][col] == "Q":
                    return False

            # explore diagonal up/down
            i, j = row, col

            while(0 <= i < n and 0 <= j < n):
                if board[i][j] == "Q":
                    return False
                i += 1
                j += 1
            
            i, j = row, col
            while(0 <= i < n and 0 <= j < n):
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            
            i, j = row, col
            while(0 <= i < n and 0 <= j < n):
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1
            
            i, j = row, col
            while(0 <= i < n and 0 <= j < n):
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            
            return True
            

        def backtrack(row):
            if row == n:

                result.append(list("".join(r) for r in board))
                return
            
            for col in range(n):
                if helper(row,col):
                    board[row][col] = "Q"

                    backtrack(row + 1)

                    board[row][col] = "."


        backtrack(0)

        return result
                



            
        

        