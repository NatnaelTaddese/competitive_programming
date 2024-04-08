class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = dict()

        left = 0
        right = 0
        # result = []

#         while right < len(nums):
#             seen[nums[right]] = seen.get(nums[right], 0) + 1

#             while len(seen) > k and left <= right:
#                 seen[nums[left]] -= 1
#                 if seen[nums[left]] == 0:
#                     del seen[nums[left]]
#                 # if len(seen) == k:
#                     # result.append([nums[left: right + 1]])
#                     # result +=1

        
#                 left += 1
            
#             if len(seen) == k:
#                 # calculate degree of fredom
#                 # if abs(right - left) > k:
#                     # result.append(right - left - k)
#                 result.append([nums[left: right + 1]])

#                 # result +=1

        

        def atMostK(nums, k):
            count = 0
            left = 0
            freq = {}

            for right in range(len(nums)):
                if nums[right] not in freq:
                    freq[nums[right]] = 0
                freq[nums[right]] += 1

                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1

                count += right - left + 1

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)

#         return result
