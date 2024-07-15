class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        def starts_with(s1, s2):
            if len(s2) > len(s1):
                return False
            
            for i in range(len(s2)):
                if not s1[i] == s2[i]:
                    return False

            return True
        
        def bactrack(num1, num2, remaining):
            if not remaining:
                return True
            
            next_num = str(int(num1) + int(num2))
            if not starts_with(remaining,next_num):
                return False
            
            return bactrack(num2, next_num, remaining[len(next_num):])
        

        for i in range(1,n):
            for j in range(i+1,n):
                num1 = num[:i]
                num2 = num[i:j]
                n1 = len(num1)
                n2 = len(num2)

                if (starts_with(num1,'0') and n1 > 1) or (starts_with(num2,'0') and n2 > 1):
                    continue
                
                elif bactrack(num1, num2, num[j:]):
                    return True
        
        return False
