class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        placeholder = 0
        next_num = 1

        while (next_num < len(nums)):
            
            if next_num >= len(nums):
                return
            
            while placeholder < len(nums):
                if nums[placeholder] == 0:
                    break
                placeholder += 1
            
            next_num = placeholder + 1

            while next_num < len(nums):
                if nums[next_num] != 0:
                    break
                next_num += 1
            if next_num >= len(nums):
                return

            # swap
            nums[placeholder], nums[next_num] = nums[next_num], nums[placeholder]