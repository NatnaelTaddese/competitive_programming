class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        # vowels = set("aeiou")
        # beautiful = ""
        # longest = 0
        
#         for char in word:
#             if not beauitful or char >= beauitful[-1]:
#                 beauitful += char
#                 if set(beauitful) == vowels:
#                     longest = max(longest, len(beauitful))
#             else:
#                 beauitful = char if char == 'a' else ""

#         return longest   

        result = 0

        curr = 1
        left = 0

        while left < len(word):
            right = left + 1

            while right < len(word) and word[right] >= word[right-1]:
                curr += 1
                right += 1

            if len(set(word[left:right])) == 5:
                result = max(result, curr)
                
            left = right
            curr = 1
        return result