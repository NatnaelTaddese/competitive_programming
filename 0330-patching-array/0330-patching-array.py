class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        total = 0
        curr = 1

        i = 0
        
        while curr <= n:
            if i < len(nums) and nums[i] <= curr:
                curr += nums[i]
                i += 1
            else:
                curr *= 2
                total += 1
        
        return total 

        