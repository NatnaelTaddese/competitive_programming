class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod_index = 0
        start = 0
        k = 0

        while(start <= len(nums) - 1):
            # if(start + 1 == )
            cursor = start + 1
            repeated = False

            while(cursor < len(nums)):
                if (nums[start] == nums[cursor]):
                    repeated = True
                    cursor += 1
                else:
                    break

            
            if repeated:
                nums[mod_index] = nums[start]
                nums[mod_index + 1] = nums[mod_index]
                mod_index += 2
            else:
                nums[mod_index] = nums[start]
                mod_index += 1

            start = cursor
            k +=1

            # problem: also need to check the last element if its ...
        
        return mod_index






