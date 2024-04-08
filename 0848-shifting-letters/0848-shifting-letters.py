class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        shifts = shifts[::-1]
        n = len(shifts)
        prefix_shift = [0] * (n + 1)

        for i in range(n):
            prefix_shift[i + 1] = prefix_shift[i] + shifts[i]
        
        prefix_shift = prefix_shift[::-1]

        # apply the addition to the string
        # for i in range(n):
        #     s[i] = chr(ord( s[i]) + (prefix_shift[i] % 26))
        
        # return s
        new_s = ""
        for i in range(n):
            new_s += chr((ord(s[i]) - ord('a') + prefix_shift[i]) % 26 + ord('a'))

        return new_s
        # [3, 5, 9]

        # [9, 5, 3]
        # [0,9, 14, 17]

        # [3, 0, 0]
        # [8, 5, 0]
        # [17, 14, 9]