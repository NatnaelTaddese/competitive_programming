class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        count = [0 for _ in range(n)]

        graph = defaultdict(list)

        for a, b in roads:
            count[a] += 1
            count[b] += 1
            graph[a].append(b)
            graph[b].append(a)

        mx = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = count[i] + count[j]
                if j in graph[i]:
                    rank -=1
                mx = max(mx, rank)
        
        return mx