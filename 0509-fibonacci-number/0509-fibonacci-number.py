class Solution(object):
    def __init__(self):
        self.mem = dict()

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n not in self.mem:
            self.mem[n] = self.fib(n-1) + self.fib(n-2)

        return self.mem[n]  


        