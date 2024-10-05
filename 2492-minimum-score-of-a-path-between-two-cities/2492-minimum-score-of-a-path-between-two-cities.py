class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(n)
        
        for a, b, dist in roads:
            uf.union(a - 1, b - 1)
        
        min_score = float('inf')
        # City 1
        root1 = uf.find(0)
        # City n
        rootN = uf.find(n - 1)  
        
        if root1 == rootN:
            for a, b, dist in roads:
                if uf.find(a - 1) == root1 and uf.find(b - 1) == root1:
                    min_score = min(min_score, dist)
        
        return min_score