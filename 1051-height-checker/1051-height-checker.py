class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = [height for height in heights]
        heights.sort()

        miss_match = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                miss_match += 1
        

        return miss_match
        