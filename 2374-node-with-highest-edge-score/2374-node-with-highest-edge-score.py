class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n = len(edges)
        scores = [0 for _ in range(n)]

        for node in range(n):
            scores[edges[node]] += node

        mx_score = -1
        mx_node = -1

        for node in range(n):
            if scores[node] > mx_score or (scores[node] == mx_score and node < mx_node):
                mx_score = scores[node]
                mx_node = node

        return mx_node  