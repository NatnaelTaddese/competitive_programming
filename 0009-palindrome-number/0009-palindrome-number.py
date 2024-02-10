class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        left = 0
        right = len(x) - 1

        flag = True

        while left < right:
            if x[left] != x[right]:
                flag = False
                break
            left += 1
            right -= 1
            
        
        return flag

        