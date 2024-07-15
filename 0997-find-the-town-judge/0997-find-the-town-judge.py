class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            if trust:
                return -1
            else:
                return 1
        
        trusted_by = [0 for _ in range(n+1)]
        trusts = [0 for _ in range(n+1)]

        for u, v in trust:
            trusts[u] += 1
            trusted_by[v] += 1
        
        for p in range(1, n + 1):
            if trusted_by[p] == n - 1 and trusts[p] == 0:
                return p
        
        return -1