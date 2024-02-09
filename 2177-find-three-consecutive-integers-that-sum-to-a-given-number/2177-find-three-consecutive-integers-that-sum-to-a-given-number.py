class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        num1 = (num - 3) // 3
        num2 = num1 + 1
        num3 = num2 + 1

        if num1 + num2 + num3 == num:
            return [num1,num2,num3]
        else:
            return []
        