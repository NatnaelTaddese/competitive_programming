class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [5 2 3 6 7 8 ]
        
        n = len(nums)
        
        dp = [1 for _ in range(n)]
        count = [1 for _ in range(n)]
        # dp[n] = 1
        longest = 1

        for i in range(n):
            for j in range(i):

                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                        
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]

            longest = max(longest, dp[i])

        return sum(count[i] for i in range(n) if dp[i] == longest)    