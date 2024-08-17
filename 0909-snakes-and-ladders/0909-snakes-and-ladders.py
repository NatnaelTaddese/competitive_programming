class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        rows, cols = len(board), len(board[0])
        destination = rows * cols
        
        def inBound(i,j):
            return 0 <= i < rows and 0 <= j < cols
        
        def getCoordinate(val):
            row = (rows - 1) - int((val - 1) / cols)
            
            remainder = ((val - 1) % cols)
            if row % 2 != rows % 2:
                col = remainder
            else:
                col = cols - 1 - remainder
            
            return row, col

        if rows == 2:
            return 1
        # step, curr
        queue = deque([(0,1)])

        # if the row is odd, we move to the left and vise versa
        # if we are out of bound we just go up
        visited = set()
        visited.add(1)

        
        while len(queue) > 0:
            # steps, r, c = queue.popleft()
            steps, curr = queue.popleft()

            # if board[r][c] == destination:
            if curr == destination:
                return steps
            
            # can skip six squares
            # i = 0
            # if r % 2 == 0:
            #     if inBound()
            for i in range(1,7):
                go_to = curr + i
                if go_to <= destination:
                    row, col = getCoordinate(go_to)
                    if board[row][col] != -1:
                        go_to = board[row][col]
                    if go_to not in visited:
                        visited.add(go_to)
                        queue.append((steps + 1, go_to))


        return -1