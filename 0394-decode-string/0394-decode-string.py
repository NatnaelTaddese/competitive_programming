class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num = 0
        current_str = ''

        # using loops
        for char in s:
            if char.isdigit():
                current_num = int(char) + current_num*10
                continue

            if char == '[':
                stack.append((current_str, current_num))
                current_str = ''
                current_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char
            
        return current_str