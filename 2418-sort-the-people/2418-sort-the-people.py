class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        ######################
        # using bubble sort

        # for i in range(len(heights)):
        #     swapped = False

        #     for j in range(0, len(heights) - i - 1):
        #         if heights[j] < heights[j + 1]:
        #             names[j], names[j+1] = names[j+1], names[j]
        #             heights[j], heights[j + 1] = heights[j + 1], heights[j]
        #             swapped = True
            
        #     if not swapped:
        #         break

        ######################
        # using insertion sort

        for i in range(1, len(heights)):
            key_height = heights[i]
            key_name = names[i]

            j = i - 1
            while j >= 0 and heights[j] < key_height:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            
            heights[j + 1] = key_height
            names[j + 1] = key_name
        
        return names
        

