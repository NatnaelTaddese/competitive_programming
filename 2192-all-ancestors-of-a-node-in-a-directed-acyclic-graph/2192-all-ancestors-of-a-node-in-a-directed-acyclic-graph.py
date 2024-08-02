class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        in_degree = [0 for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        roots = []
        for i in range(n):
            if in_degree[i] == 0:
                roots.append(i)
        
        print(roots)
        
        ancestors = [set() for _ in range(n)]

        queue = deque(roots)

        while queue:
            node = queue.popleft()
            print(node)
            for neighbor in graph[node]:
                # append the node to the ancestor list
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)

                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        result = []
        for ancestor in ancestors:
            result.append(sorted(ancestor)) 
        
        return result 

        
        