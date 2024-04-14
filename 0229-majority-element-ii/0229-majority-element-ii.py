class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        target = len(nums) // 3
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        result = []
        for num, frequency in freq.items():
            if frequency > target:
                result.append(num)
                # only two elements at most can fulfill the criteria 
                if len(result) >= 2:
                    break
        return result
        