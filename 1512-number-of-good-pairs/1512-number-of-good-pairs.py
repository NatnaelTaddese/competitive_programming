class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_good_pairs = 0
        good_pairs = set()

        for i in range(len(nums) - 1):
           for j in range(i + 1, len(nums)):
               if nums[i] == nums[j] and (i, j) not in good_pairs:
                   n_good_pairs += 1
                   good_pairs.add((i, j))

        return n_good_pairs