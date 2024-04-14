class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs = 0
        seen_pairs = set() # keeps track of the pairs, to remove redundant pairs

        for i in range(len(nums) - 1):
           for j in range(i + 1, len(nums)):
               if nums[i] == nums[j] and (i, j) not in seen_pairs:
                   good_pairs += 1
                   seen_pairs.add((i, j))

        return good_pairs