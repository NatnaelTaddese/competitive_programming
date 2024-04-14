class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """

        # if the data was sorted:
    
        # def binary_search(arr, key):
        #     left = 0
        #     right = len(arr) - 1

        #     while left <= right:
        #         mid = (left + right) // 2
        #         if arr[mid] == key:
        #             return mid
        #         elif arr[mid] < key:
        #             left = mid + 1
        #         else:
        #             right = mid - 1

        #     return -1

        # for operation in operations:
        #     # index = nums.index(operation[0])     
        #     # time limit exceeded
        #     index = binary_search(nums, operation[0])
        #     nums[index] = operation[1]
        
        # return nums

        num_indices = {}
        for i, num in enumerate(nums):
            if num not in num_indices:
                num_indices[num] = [i]
            else:
                num_indices[num].append(i)
        
        for operation in operations:
            num = operation[0]
            new_num = operation[1]
            if num in num_indices:
                for index in num_indices[num]:
                    nums[index] = new_num
                num_indices[new_num] = num_indices.get(new_num, []) + num_indices[num]
                del num_indices[num]
        
        return nums