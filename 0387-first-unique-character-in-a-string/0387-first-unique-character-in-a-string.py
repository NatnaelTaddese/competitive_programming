class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = defaultdict(int)

        # pre-proccess
        for char in s:
            seen[char] = seen[char] + 1
        
        # actual finding
        for i in range(0,len(s)):
            if seen[s[i]] == 1:
                return i
        
        return -1
