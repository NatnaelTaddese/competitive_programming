class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def bactrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                # //why is it not commenting this?
                path.append(nums[i])
                bactrack(i + 1, path)
                path.pop()

        bactrack(0,[])

        return result