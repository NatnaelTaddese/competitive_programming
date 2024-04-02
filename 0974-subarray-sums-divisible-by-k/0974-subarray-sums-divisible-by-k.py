class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        remainders = [0] * k
        remainders[0] = 1

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum < 0:
                prefix_sum += k
            count += remainders[prefix_sum]
            remainders[prefix_sum] += 1
        
        return count
        
        