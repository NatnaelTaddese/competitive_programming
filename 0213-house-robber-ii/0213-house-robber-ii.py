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
        if n == 1:
            return nums[0]
        
        def helper(option):
            mem = dict()
            return self.dp(mem, option, len(option) - 1)

        option1 = nums[:-1]
        option2 = nums[1:]

        # print(option1, option2)
        return max(helper(option1), helper(option2))
        