class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = -1

        # [2,1,6,4]
        # sum of the even: 5
        # sum of the odd: 8
        '''
        index 0 even: even = odd -  
        index 1 odd:
        index 2 even:
        index 3 odd:

        '''
        # sum_even = 0
        # for i in range(0,len(nums),2):
        #     sum_even += nums[i]
        
        # sum_odd = 0
        # for i in range(1,len(nums), 2):
        #     sum_odd += nums[i]

        count = 0
        sum_even = sum(nums[::2])  
        sum_odd = sum(nums[1::2])
        
        # isEven = True
        # for i in range(len(nums)):
        #     isEven = not isEven

        #     if isEven:
        #         if sum_odd == sum_even - nums[i]:
        #             return i
        #         #
        #     else:
        #         # pass
        #         if sum_even == sum_odd - nums[i]:
        #             return i
        
        count = 0

        for i in range(len(nums)):
            if i % 2 == 0:  # removing an even-indexed element
                sum_even -= nums[i]
            else:  # removing an odd-indexed element
                sum_odd -= nums[i]

            if sum_even == sum_odd:
                # Im dumb, I'm supposed to return the count of the indexes, not the index itself
                # return i
                count += 1
            
            if i % 2 == 0:
                sum_even -= nums[i]
            else:
                sum_odd -= nums[i]
  
        return count
