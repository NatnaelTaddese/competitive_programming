class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive_numbers = []
        negative_numbers = []

        for num in nums:
            if num < 0:
                negative_numbers.append(num)
            else:
                positive_numbers.append(num)

        # constructing the new array
        
        result = []

        for i in range(len(positive_numbers)):
            result.append(positive_numbers[i])
            result.append(negative_numbers[i])
        
        return result
