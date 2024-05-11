class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def generateString(n):
            if n == 1:
                return "0"
            prev = generateString(n - 1)
            return prev + "1" + ''.join('1' if c == '0' else '0' for c in reversed(prev))

        return generateString(n)[k - 1]