class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        left = 0
        right = 0
        deletion = 0  
        
        while right < len(nums):
            if nums[right] == 0:
                deletion += 1

            while deletion > 1:  
                if nums[left] == 0:
                    deletion -= 1
                left += 1
            
            longest = max(longest, right - left) 
            right += 1
        
        return longest
