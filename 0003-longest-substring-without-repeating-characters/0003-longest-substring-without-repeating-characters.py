class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = dict()

#         left = 0
#         right = left + 1
#         seen[left] = 1
#         longest = 0

#         while (right < len(s)):
#             if s[right] not in seen:
#                 seen[right] = 1
#                 right += 1
#                 longest += 1
#                 continue
#             else:
#                 seen[left] -= 1
#                 if seen[left] == 0:
#                     del seen[left]
#                 left += 1
#                 longest -= 1
        
#         return longest
        
        left = 0  
        right = 0  
        
        longest = 0 
        
        while right < len(s):
            if s[right] not in seen or seen[s[right]] < left:
                # If the current character is not in the seen dictionary
                # or its index is less than the left pointer, it's a new character in the substring
                # Increment right pointer and update the longest substring length
                seen[s[right]] = right
                right += 1
                longest = max(longest, right - left)
            else:
                # If the current character is already seen in the current substring
                # Update the left pointer to the next index of the repeated character
                # Update the seen dictionary accordingly
                left = seen[s[right]] + 1
                seen[s[right]] = right
                right += 1
        
        return longest
