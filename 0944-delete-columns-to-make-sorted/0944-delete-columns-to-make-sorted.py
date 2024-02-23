class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        result = 0

        rows = len(strs)
        cols = len(strs[0])

        for j in range(cols):
            isSorted = True
            for i in range(rows - 1):
                if strs[i][j] > strs[i + 1][j]:
                    isSorted = False
                    result += 1
                    break
    
        return result