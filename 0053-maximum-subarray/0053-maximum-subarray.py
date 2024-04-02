class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # keeps track of the minumun 
        min_val = float('inf')

        result = float('-inf')

        for right in range(1, len(nums) + 1):
            left = right - 1
            min_val = min(min_val, prefix_sum[left])
            curr_sum = prefix_sum[right] - min_val 
            result = max(result, curr_sum)
        
        return result
