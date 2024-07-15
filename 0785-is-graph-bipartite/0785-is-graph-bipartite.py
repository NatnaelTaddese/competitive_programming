class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = [-1 for _ in range(len(graph))]
        
        def dfs(node, depth):
            
            # the node represents its depth
            visited[node] = depth

            for neighbor in graph[node]:
                # hasnt been visited
                if visited[neighbor] == -1:
                    if not dfs(neighbor, depth + 1):
                        return False
            
                # this means there is a cycle
                # if its even then it is bipartete
                elif (depth - visited[neighbor]) % 2 == 0:
                    return False
            
            return True
        
        
        # Check each component of the graph
        for i in range(len(graph)):
            if visited[i] == -1:
                if not dfs(i, 0):
                    return False
        
        return True