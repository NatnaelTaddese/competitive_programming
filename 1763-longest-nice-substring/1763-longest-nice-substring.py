class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""

        def is_nice(sub):
            chars = set(sub)
            
            for char in chars:
                if char.swapcase() not in chars:
                    return False

            return True 



        def backtrack(s):
            if len(s) < 2:
                return ""
            
            if is_nice(s):
                return s
            
            mx_nice = ""
            unique = set(s)
            for i in range(len(s)):
                if s[i].swapcase() not in unique:
                    left = backtrack(s[:i])
                    right = backtrack(s[i+1:])

                    if len(left) >= len(right):
                        return left
                    else:
                        return right

                # print(left, right)

                # if len(left) >= len(mx_nice):
                #     mx_nice = left
                
                # if len(right) > len(mx_nice):
                #     mx_nice = right
            
            return s
                
        return backtrack(s)
        
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):

        #         curr = s[i:j+1]
        #         if (j - i) > len(result) + 1 and is_nice(s[i:j+1]) :
        #             result = curr
        
        # return result

