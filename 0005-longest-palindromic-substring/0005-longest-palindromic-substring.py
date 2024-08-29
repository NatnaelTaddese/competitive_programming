class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(left, right):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            return left + 1, right
        
        if len(s) == 0:
            return ""

        start = 0
        end = 0
        for i in range(len(s)):
            odd_left, odd_right = expand(i,i)

            even_left, even_right = expand(i, i + 1)

            #debug
            print("odd: ", odd_left, odd_right)
            print("even: ", even_left, even_right)

            if odd_right - odd_left > end - start:
                start, end = odd_left, odd_right
            if even_right - even_left > end - start:
                start, end = even_left, even_right
            
        
        return s[start:end]