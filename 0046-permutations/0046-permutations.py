class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = []
        # n = len(nums)

        # def bactrack(start, end):
        #     if start == end:
        #         result.append(nums[:])
        #         return
        #     for i in range(start, end):


        # return result
        return list(itertools.permutations(nums))