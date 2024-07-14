class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(mat), len(mat[0])
        distances = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    distances[i][j] = 0

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if distances[nx][ny] > distances[x][y] + 1:
                        distances[nx][ny] = distances[x][y] + 1
                        queue.append((nx, ny))

        return distances