class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        """
        create a graph with the edge being the weight(v)

        """

        graph = defaultdict(dict)
        result = []

        for i in range(len(values)):
            a,b = equations[i]
            value = values[i]

            graph[a][b] = value
            graph[b][a] = 1 / value
        
        #debug
        # print(graph)

        #BFS ..
        def bfs(i,j):
            if i not in graph or j not in graph:
                return -1.0

            queue = deque([(i, 1.0)])
            visited = set()

            while queue:
                curr, prd = queue.popleft()

                # end is reached
                if curr == j:
                    return prd
                
                visited.add(curr)

                for neighbor, val in graph[curr].items():
                    if neighbor not in visited:
                        queue.append((neighbor, prd * val))
        
            return -1.0

        for c,d in queries:
            #bfs the result
            result.append(bfs(c,d))
        
        # print(result)

        return result
        # return []

