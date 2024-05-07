class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            
            stack.append(num)
        
        #construct the answer into a single array
        result = []
        for num in nums1:
            result.append(next_greater[num])
        
        return result