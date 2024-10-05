class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def count(a):
            ones = 0
            
            while a:
                ones += a & 1
                a >>= 1
            
            return ones
        
        result = [ 0 for _ in range(n + 1)]
        
        for i in range(n + 1):
            result[i] = count(i)
        
        return result