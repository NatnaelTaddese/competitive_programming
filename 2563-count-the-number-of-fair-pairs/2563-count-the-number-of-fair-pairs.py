class Solution(object):

    def find_left_bound(self,nums, target, start):
        lo, hi = start, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def find_right_bound(self,nums, target, start):
        lo, hi = start, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        # 0 1 4 4 5 7
        # 1 2 3 : 1 2, 1 3, 1 2 3 
        
        '''
        N * (N + 1)/2
        0: from 2 - 3 : how many sub pairs can we create in this window?
        1: from 2 - 4 :
        '''
        # 0 1 5 9 14 21 

        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1

            # find lower bound
            # while left < len(nums) - 1:
            #     if nums[i] + nums[left] > lower:
            #         left +=1
            
            left_bound = self.find_left_bound(nums, lower - nums[i], i + 1)
            
            # find higher bound
            # while right > 0:
            #     if nums[i] + nums[right] < upper:
            #         right -= 1
            
            right_bound = self.find_right_bound(nums, upper - nums[i], i + 1) - 1
            
            # ans += (right_bound - left_bound) * ((right_bound - left_bound) + 1) / 2
            if left_bound <= right_bound:
                ans += (right_bound - left_bound + 1)
        
        return ans
