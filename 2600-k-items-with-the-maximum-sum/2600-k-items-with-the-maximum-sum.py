class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        result = 0

        if k > numOnes:
            #
            result += numOnes
            k -= numOnes
            if k > numZeros:
                k -= numZeros
                if k > 0:
                    result -= k 
        else:
            result = k
        
        return result