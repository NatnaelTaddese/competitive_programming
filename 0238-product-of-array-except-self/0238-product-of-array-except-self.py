class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        r_prd = [1] * n 

        total_prd = 1

        for i in range(n):
            r_prd[i] *= total_prd
            total_prd *= nums[i]

        total_prd = 1

        for i in range(n - 1, -1, -1):
            r_prd[i] *= total_prd
            total_prd *= nums[i]

        return r_prd