class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix_sum = [0] * (len(nums) + 1)

        # for i in range(len(nums)):
        #     prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        prefix_sum = {0: 1}

        left = 0

        count = 0

        # while(left < len(nums)):
        #     right = left + 1
        #     while ( right < len(nums) + 1):
        #         if prefix_sum[right] - prefix_sum[left -  1] == k:
        #             # k = a(left) - b(right)
        #             count += 1
        #         right += 1
        #     left += 1


        current_sum = 0

        for num in nums:

            current_sum += num
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]    
            
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1


        
        return count 
        # 1 2 3
