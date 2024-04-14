class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        keyboard = [first_row, second_row, third_row]

        result = []

        for word in words:
            typed = True
            row = 0
            #sanitize word
            sanitized = word.lower()
            # first character of the word determines the row
            if sanitized[0] in first_row:
                row = 0
            elif sanitized[0] in second_row:
                row = 1
            else:
                row = 2
            
            for c in sanitized:
                if c not in keyboard[row]:
                    typed = False
                    break

            if typed:
                result.append(word)

        return result


        