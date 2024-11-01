class Solution:
    def makeFancyString(self, s: str) -> str:
        last_seen = s[0]
        consecutive = 0

        result = ""
        for c in s:
            if c == last_seen:
                consecutive += 1
            else:
                last_seen = c
                consecutive = 1
            
            if consecutive < 3:
                result = result + c
        
        return result


        