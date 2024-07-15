class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            stack = [city]

            while stack:
                current = stack.pop()
                for neighbor in range(n):
                    if isConnected[current][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1
        

        return provinces
            