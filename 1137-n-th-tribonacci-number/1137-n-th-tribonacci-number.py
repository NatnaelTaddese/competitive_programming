class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brute force
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # one indexed
        fib = [0 for _ in range(n + 1)]
        fib[0], fib[1], fib[2] = 0, 1, 1

        # construct the fib
        for i in range(3, n + 1):
            # Tn+3 = Tn + Tn+1 + Tn+2 
            fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3]
        
        return fib[n]