class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result = []

        # find elments less than
        for num in nums:
            if num < pivot:
                result.append(num)
        # find elements in between
        for num in nums:
            if num == pivot:
                result.append(num)

        # finf elements greater than
        for num in nums:
            if num > pivot:
                result.append(num)
        
        return result