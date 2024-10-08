class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        # making sure if we actually can acheive the target
        # for example for the test case [1] : 2
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0

        target_sum = (total_sum + target) // 2

        dp = [0 for _ in range(target_sum + 1)]
        dp[0] = 1
        
        for num in nums:
            for i in range(target_sum, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[target_sum]