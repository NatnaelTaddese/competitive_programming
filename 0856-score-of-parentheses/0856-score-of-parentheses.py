class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        score = 0

        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score * 2, 1)

        return score
        