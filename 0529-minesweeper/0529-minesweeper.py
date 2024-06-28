class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # seen = [[False] for _ in range(len(board[0])) ] for _ in rangelen((board[0]))
        # def dfs(row, col):
        #     if seen[row,col]:
        #         return

        #     seen[row,col] = True
            
        #     if board[row][col] == 'M':
        #         return
        #     if board[row][col] == 

        def dfs(board, row, col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            
            if board[row][col] != 'E':
                return
            
            mines_count = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'M':
                    mines_count += 1
            
            if mines_count > 0:
                board[row][col] = str(mines_count)
            else:
                board[row][col] = 'B'
                for dr, dc in directions:
                    dfs(board, row + dr, col + dc)

        
        
        click_row, click_col = click
        
        if board[click_row][click_col] == 'M':
            board[click_row][click_col] = 'X'
        else:
            dfs(board, click_row, click_col)
        
        return board





        