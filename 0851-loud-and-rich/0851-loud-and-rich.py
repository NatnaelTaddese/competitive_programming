class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        n = len(quiet)
        in_degree = [0 for _ in range(n)]

        for u, v in richer:
            graph[u].append(v)
            in_degree[v] += 1
        
        roots = []
        for i in range(n):
            if in_degree[i] == 0:
                roots.append(i)
        
        result = list(range(n))

        queue = deque(roots)

        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if quiet[result[node]] < quiet[result[neighbor]]:
                    result[neighbor] = result[node]
                
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result