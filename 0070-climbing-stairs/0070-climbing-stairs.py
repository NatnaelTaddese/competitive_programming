# from math import comb

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # total_ways = 0
        # max_two_steps = n // 2
        # for k in range(max_two_steps + 1):
        #     total_ways += Math.comb(n - k, k)
        # return total_ways

        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


        # if n == 0:
        #     return 1
        # elif n == 1:
        #     return 1
        
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        
        # for i in range(2, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]