class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        smallest_word_length = len(strs[0])

        for word in range(0,len(strs)):
            if len(strs[word]) < smallest_word_length:
                smallest_word_length = len(strs[word])

        for i in range(0, smallest_word_length):
            key = (strs[0])[i]
            flag = True
            for word in strs:
                if word[i] != key:
                    flag = False
                    break
            if flag:
                result += key
            else:
                break
        
        return result
