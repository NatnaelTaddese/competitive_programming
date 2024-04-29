class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # left = 0
        # right = 0

        # while left < len(nums):
        stack = []
        third_val = float('-inf')
        nums = reversed(nums)


        for num in nums:
            if num < third_val:
                return True
            
            while stack and stack[-1] < num:
                third_val = stack.pop()
            
            stack.append(num)
        
        return False
