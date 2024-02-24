class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numbers = "".join( str(num) for num in digits)

        result = str( int(numbers) + 1 )

        return [ int(num) for num in result ]
