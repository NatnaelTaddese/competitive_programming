class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = []

        for i in range(len(words) - 1, -1, -1):
            result.append(words[i])
        
        return ' '.join(result)
        