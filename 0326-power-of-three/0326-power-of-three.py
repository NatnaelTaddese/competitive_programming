class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # base cases:
        if n == 1:
            return True
        elif n < 1  or n % 3 != 0:
            return False
        else:
            return self.isPowerOfThree(n / 3)