class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        in_degree = [0 for _ in range(n)]
        
        for edge in edges:
            from_node, to_node = edge
            in_degree[to_node] += 1
        
        
        
        return [i for i in range(n) if in_degree[i] == 0]