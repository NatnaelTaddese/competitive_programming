class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        placeholder = 0
    
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != placeholder:
                    nums[placeholder], nums[i] = nums[i], nums[placeholder]
                placeholder += 1