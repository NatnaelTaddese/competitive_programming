class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        seen = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                seen[i + j].append(mat[i][j])
        
        output = []
        for i in range(0, (len(mat) + len(mat[0]) - 1) ):
            if i % 2 == 0:
                output.extend(seen[i][::-1])
            else:
                output.extend(seen[i])

        return output
        