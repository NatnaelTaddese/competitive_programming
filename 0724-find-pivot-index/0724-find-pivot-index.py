class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # l_sum = [0]
        # for num in nums:
        #     l_sum.append(num + l_sum[-1])

        # r_sum = [0]
        # for i in range(len(nums) - 1, -1, -1):
        #     r_sum.append(nums[i] + r_sum[-1])

        # # r_sum.reverse()  # Reverse r_sum to match the original order of the array

        # for i in range(len(nums)):
        #     if l_sum[i] == r_sum[i]:
        #         return i
        
        # return [l_sum, r_sum]
        # # return i+1

        prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for i in range(len(nums)):
            if prefix_sum[i] == prefix_sum[-1] - prefix_sum[i + 1]:
                return i

        return -1