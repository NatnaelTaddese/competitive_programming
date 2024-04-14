class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = []

        i = 0
        while (i < len(chars)):
            j = i
            length = 0
            while( j < len(chars)):
                if chars[i] == chars[j]:
                    length += 1
                    j += 1
                else:
                    break
            if length < 2:
                result.append(chars[i])
            else:
                result.append(chars[i])
                result.append(str(length))
            i = j
        
        result = "".join(result)

        for i in range(len(result)):
            chars[i] = result[i]
        
        return len(result)


            
        