class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        position_left = -1
        position_right = -1

        # find starting from left
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        position_left = left

        # find starting from right

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        position_right = right

        # check if it existed

        if position_left > position_right:
            return [-1,-1]

        return [position_left,position_right]
        
        