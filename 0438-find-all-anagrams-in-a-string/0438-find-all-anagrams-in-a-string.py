class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count = Counter(p)

        left = 0
        right = left + len(p) - 1

        s_count = Counter(s[left:right+1])

        result = []

        # while( right < len(s)):
        #     s_count[s[left]] = s_count.get(s[left]) - 1
        #     s_count[s[right]] = s_count.get(s[right],0) + 1


        #     if p_count == s_count:
        #         result.append(left)

        #     left += 1
        #     right += 1
        
        # return result

        while right < len(s):
            if p_count == s_count:
                result.append(left)

            s_count[s[left]] -= 1
            # we have to delete the key if the value is zero
            # or else it will cause issues when comapring the p_count and the s_count
            # since if the count is zero, we no longer need it
            if s_count[s[left]] == 0:
                del s_count[s[left]]

            right += 1
            if right < len(s):
                s_count[s[right]] = s_count.get(s[right], 0) + 1

            left += 1

        return result
        