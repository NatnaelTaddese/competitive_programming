class Solution(object):

    def generateRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev_row = self.generateRow(rowIndex - 1)
            row = [1]
            for i in range(1, len(prev_row)):
                row.append(prev_row[i - 1] + prev_row[i])
            row.append(1)
            return row
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.generateRow(rowIndex)
        