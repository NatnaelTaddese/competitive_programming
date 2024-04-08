class NumArray(object):
    r_sum = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.r_sum.append(nums[0])

        for i in range(1, len(nums)):
            self.r_sum.append(nums[i] + self.r_sum[-1])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.r_sum[right]
        else:
            return self.r_sum[right] - self.r_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)