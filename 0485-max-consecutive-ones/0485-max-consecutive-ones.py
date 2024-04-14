class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consecutive = 0
        c_max = 0
        for num in nums:
            if num == 1:
                consecutive += 1
            else:
                consecutive = 0
            
            if c_max < consecutive:
                c_max = consecutive
        
        return c_max
        