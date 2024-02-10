class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        super_string = ""
        if len(word1) > len(word2):
            flag = True
            length = len(word2)
        else:
            flag = False
            length = len(word1)
        
        for i in range(0, length):
            super_string += word1[i]
            super_string += word2[i]

        if flag:
            super_string += word1[length:len(word1)]
        else:
            super_string += word2[length:len(word2)]

        return super_string
