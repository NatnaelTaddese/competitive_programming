class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # i = 0
        # j = 1
        # k = 2
        # while j < len(nums):
        #     if nums[j] < nums[i]:
        #         # violation
        #         if j + 1 <= len(nums) + 1:
        #             k = j + 1
        #             if nums[k] > nums[i]:
        #                 violation += 1
        #             else:
        #                 return False
        #             nums[j] = nums[i]
        #         else:
        #             if violation > 1:
        #                 return False
        #             else:
        #                 break
        #     i += 1
        #     j += 1
        # return True

        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
        return True



