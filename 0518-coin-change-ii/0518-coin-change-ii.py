class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        memo = [0 for _ in range(amount + 1)]
        memo[0] = 1


        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] += memo[i - coin]
        

        return memo[amount]

        