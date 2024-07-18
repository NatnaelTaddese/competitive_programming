class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        # i = 1
        # while i < len(nums) - 1:
        #     if nums[i] > nums[i - 1]:
        #         nums[i] = 
        i = len(nums) - 2

        while i >= 0:
            if nums[i] > nums[i+1]:
                # if i > 0 and nums[i] < nums[i - 1]:
                #     nums[i] =  nums[i] // 2
                #     operations += 1
                # else:
                #     nums[i] = nums[i] - nums[i+1]
                #     operations += 1
                operation = (nums[i] + nums[i+1] - 1) / nums[i+1]
                nums[i] = nums[i] // operation

                operations += operation - 1
            else:
                i -= 1

        return operations

'''
[1,2,7,5]
[1,2,5,5]

[1,2,2,5,5]

[1,2,7,6]
[1,9,7,6]

[12,9,7,6,17,19,21]
[12,[1,1,1,1,1,1,1,1,1],[1,6],6,17,19,21]
'''