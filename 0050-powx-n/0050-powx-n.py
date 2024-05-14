class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        #if n is negative, cals resprocal
        if n < 0:
            x = 1 / x
            n = abs(n)
        

        # if we dont slice the operation in half
        # it will casue recussion limit error
        # so we divide the power into half and mutliply it again to get result
        half = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        
        else:
            return half * half * x