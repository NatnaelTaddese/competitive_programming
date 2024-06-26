class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        result = []

        while (left < right):
            if numbers[left] + numbers[right] == target:
                result.append(left + 1)
                result.append(right + 1)
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        
        return result
        