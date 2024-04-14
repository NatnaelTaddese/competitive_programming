class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        # first = 0
        # second = 0
        # result = []

        # while(first <= len(firstList) - 1 and second <= len(secondList) - 1):
        #     segment = []
        #     # if firstList[first][0] < :
        #     #     # fininsh
        #     # else:
        #     #     # finish
            
        #     # if 
        #     i = max(firstList[first][0],secondList[second][0])
        #     j = min(firstList[first][1],secondList[second][1])

        #     segment
        
        # firstList.sort(key=lambda x: x[0])
        # secondList.sort(key=lambda x: x[0])

        # i, j = 0, 0
        # while i < len(firstList) and j < len(secondList):
        #     intersection = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])
        #     if intersection:
        #         firstList[i] = intersection
        #         secondList[j] = intersection
        #         i += 1
        #         j += 1
        #     elif firstList[i][0] < secondList[j][0]:
        #         i += 1
        #     else:
        #         j += 1

        # return firstList
        result = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                result.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result