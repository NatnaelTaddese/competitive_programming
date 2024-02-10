class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        seen = {}
        # create a hash map of the word to then compare if a letter is added
        for letter in s:
            seen[letter] = seen.get(letter, 0) + 1

        for letter in t:
            if letter not in seen or seen[letter] == 0:
                return letter
            seen[letter] -= 1

        return ""
        