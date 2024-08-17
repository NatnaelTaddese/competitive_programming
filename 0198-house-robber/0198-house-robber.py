class Solution(object):
    
    def dp(self,mem,nums,i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        if i not in mem:
            mem[i] =  max(self.dp(mem, nums, i - 1), nums[i] + self.dp(mem, nums, i - 2))

        return mem[i]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mem = dict()

        if n == 1:
            return nums[0]

        
        return max(self.dp(mem, nums, n - 1), self.dp(mem,nums, n - 2))

        