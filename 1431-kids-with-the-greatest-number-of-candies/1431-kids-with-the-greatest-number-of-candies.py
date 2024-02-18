class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []

        for candy in candies:
            br = True
            for other in candies:
                if candy + extraCandies < other:
                    result.append(False)
                    br = False
                    break
            if br == True:
                result.append(True)

        return result
            