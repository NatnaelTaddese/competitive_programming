class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        dp_hold = [0 for _ in range(n)]
        dp_sell = [0 for _ in range(n)]
        dp_cool = [0 for _ in range(n)]

        dp_hold[0] = -prices[0]

        for i in range(1, n):
            dp_hold[i] = max(dp_hold[i-1], dp_cool[i-1] - prices[i])
            dp_sell[i] = dp_hold[i-1] + prices[i]
            dp_cool[i] = max(dp_cool[i-1], dp_sell[i-1])
        
        return max(dp_sell[-1], dp_cool[-1])