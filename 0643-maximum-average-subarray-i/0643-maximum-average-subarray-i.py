class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        right = left + k

        max_sum = sum(nums[:k])
        max_window_sum = max_sum


        while right < len(nums):
            max_sum = max_sum - nums[left] + nums[right]
            max_window_sum = max(max_window_sum, max_sum) 
            left += 1
            right += 1

        return float(max_window_sum) / float(k)