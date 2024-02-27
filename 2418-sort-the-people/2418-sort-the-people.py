class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(len(heights)):

            swapped = False
            for j in range(0, len(heights) - i - 1):
                if heights[j] < heights[j + 1]:
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    swapped = True
            
            if not swapped:
                break
        
        return names
        