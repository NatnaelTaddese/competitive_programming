class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        smallest_word_length = len(strs[0])

        # pre-process the data:
        # find the smallest word length
        for word in strs:
            if len(word) < smallest_word_length:
                smallest_word_length = len(word)


        # compare each letter
        for letter in range(0, smallest_word_length):
            
            key = (strs[0])[letter] # inistializes the first words letter as the key and compare the others to this
            flag = True

            for word in strs:
                if word[letter] != key:
                    flag = False
                    break
            if flag:
                result += key
            else:
                break
        
        return result
