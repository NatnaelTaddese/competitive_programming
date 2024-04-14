class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        exist = dict()
        result = []
        for i in range(len(nums)):
            if target - nums[i] in exist:
                result.append(exist[target - nums[i]])
                result.append(i)
                break
            else:
                exist[nums[i]] = i
            
        return result