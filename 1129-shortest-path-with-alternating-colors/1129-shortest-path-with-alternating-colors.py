class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)
        
        result = [ -1 for _ in range(n)]
        result[0] = 0

        queue = deque([(0, 'red'), (0, 'blue')]) 
        visited = set((0, 'red')) | set((0, 'blue'))

        level = 0

        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                
                if color == 'red':
                    next_color = 'blue'
                    next_nodes = blue_adj[node]
                else:
                    next_color = 'red'
                    next_nodes = red_adj[node]
                
                for next_node in next_nodes:
                    if (next_node, next_color) not in visited:
                        visited.add((next_node, next_color))
                        queue.append((next_node, next_color))

                        if result[next_node] == -1:
                            result[next_node] = level + 1
                            
            level += 1
        
        return result