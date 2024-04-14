class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        result = [0 for _ in range(len(nums))]

        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                result[index] = nums[i]
                index+= 1
        
        return result

        