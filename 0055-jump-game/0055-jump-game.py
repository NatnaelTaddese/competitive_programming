class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # def backtrack(position):
        #     if position == len(nums) - 1:
        #         return True

        #     furthest_jump = min(position + nums[position], len(nums) - 1)

        #     for next_position in range(position + 1, furthest_jump + 1):
        #         if backtrack(next_position):
        #             return True

        #     return False

        # return backtrack(0)
        mx_reachable = 0
        
        for i in range(len(nums)):
            if i > mx_reachable:
                return False
            
            mx_reachable = max(mx_reachable, i + nums[i])
            
            if mx_reachable >= len(nums) - 1:
                return True
        
        return False