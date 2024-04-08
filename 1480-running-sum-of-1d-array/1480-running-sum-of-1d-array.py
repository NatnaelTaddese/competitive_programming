class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r_sum = []
        r_sum.append(nums[0])

        for i in range(1, len(nums)):
            r_sum.append(nums[i] + r_sum[-1])

        return r_sum
        