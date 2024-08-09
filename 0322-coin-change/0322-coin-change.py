class Solution(object):
    def dp(self, target):
        if target == 0:
            return 0

        if target < 0:
            return float('inf')

        if target in self.coinsTomake:
            return self.coinsTomake[target]
        
        # no skip or skip
        # self.coinsTomake[target] = min(
        #     self.dp(index+1, target % self.coins[index]),
        #     self.dp(index+1, target)
        #     )

        min_coins = float('inf')
        for coin in self.coins:
            min_coins = min(min_coins, 1 + self.dp(target - coin))

        self.coinsTomake[target] = min_coins
        
        return self.coinsTomake[target]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.coinsTomake = dict()
        self.n = len(coins)
        self.coins = coins

        result = self.dp(amount)

        return result if result != float('inf') else -1