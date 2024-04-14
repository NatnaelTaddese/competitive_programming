class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = 0
        
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                result.append(chr(int(s[i:i+2]) + ord('a') - 1))
                i += 3
            else:
                result.append(chr(int(s[i]) + ord('a') - 1))
                i += 1

        return ''.join(result)

        