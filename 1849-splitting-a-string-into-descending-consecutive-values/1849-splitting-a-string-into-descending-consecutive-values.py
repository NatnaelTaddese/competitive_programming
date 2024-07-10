class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        def bactrack(prev, index):
            if index == n:
                return True
            
            num = 0
            for i in range(index, n):
                num = (num * 10) + int(s[i])
                if num == prev - 1:
                    if bactrack(num, i+1):
                        return True
            
            return False

        
        for i in range(1, n):
            num = int(s[:i])
            if bactrack(num,i):
                return True
        

        return False

        