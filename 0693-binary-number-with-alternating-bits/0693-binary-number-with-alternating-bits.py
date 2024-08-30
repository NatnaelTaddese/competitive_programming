class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # length = n.bit_length()
        # mask = (1 << length) - 1

        b_rep = str(bin(n))

        for i in range(len(b_rep) - 1):
            if b_rep[i] == b_rep[i+1]:
                return False
        
        return True

        