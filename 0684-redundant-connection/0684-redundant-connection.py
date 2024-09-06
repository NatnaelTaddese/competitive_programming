class Solution(object):
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
        
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
        else:
            return True
        
        return False
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

        # answer = [0,0]
        # seen = set()
        # for edge in edges:
        #     if edge[0] in seen and edge[1] in seen:
        #         answer[0] = edge[0]
        #         answer[1] = edge[1]
        #     seen.add(edge[1])
        #     seen.add(edge[0])

        # return answer
        

        answer = []

        for edge in edges:
            print(edge)

            if self.union(edge[0],edge[1]):
                answer = edge[:]
        
        return answer

