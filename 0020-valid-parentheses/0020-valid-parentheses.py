class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_brace = {'(':')', '{':'}','[':']'}
        close_brace = {')':'(', '}':'{',']':'['}


        # this will work if we think the parenthesis of 
        # seen = {'(':0, '{':0,'[':0}
        # for c in s:
        #     if c in open_brace:
        #         seen[c] += 1
        #     elif c in close_brace:
        #         seen[close_brace[c]] -= 1
        #         if seen[close_brace[c]] < 0:
        #             print(seen[close_brace[c]])
        #             return False
        

        # return True

        stack = []
        braces = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in braces:
                if stack:
                    top = stack.pop() 
                else:
                    top = None
                if braces[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack

        