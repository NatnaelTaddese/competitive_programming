class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
#         seen = dict()

#         left = 0
#         right = len(s) - 1
#         partitions = []
#         result = []


#         while(left < right):
#             if s[left] == s[right]:
#                 partitions.append(s[left:right+1])
#                 left = right
#                 right = len(s) - 1
#             else:
#                 right -= 1
    
#             if left == right:
#                 left += 1
#                 right = len(s) - 1

        
#         for partition in partitions:
#             result.append(len(partition))

#         return partitions

        last_seen = {c: i for i, c in enumerate(s)}

        partitions = []
        left = 0
        right = 0

        for i, c in enumerate(s):

            right = max(last_seen[c], right)
            if i == right:
                partitions.append(right - left + 1)
                left = i + 1

        return partitions
