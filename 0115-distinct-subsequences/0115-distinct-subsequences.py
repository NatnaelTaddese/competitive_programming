class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        memo = dict()

        def dp(i, j):
            # i: for s
            # j: for t
            if j == 0:
                return 1
            if i == 0:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            # relation: pick unpick
            if s[i - 1] == t[j - 1]:
                memo[(i,j)] = dp(i - 1, j - 1) + dp(i - 1, j)
            else:
                memo[(i,j)] = dp(i - 1, j)
            
            return memo[(i,j)]

        return dp(m,n)