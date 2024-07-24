class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        '''
        [1,1,3] [2,3,4]
        
        1 2
        1  ... 10 
        '''
        min_heap = []        

        # for num in nums1:
        #     for num2 in nums2:
        #         heappush(min_heap, ((num + num2), num, num2))
        for i in range(min(len(nums1), k)):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0 ))

        # min_heap.sort(key = lambda x: x[0])

        # return min_heap
        result = []
        # print(min_heap)

        # for i in range(k):
            # result.append([min_heap[i][1],min_heap[i][2]])
        while min_heap and len(result) < k:
            sm, i, j = heappop(min_heap)
            # print(nums1[i],nums2[j])
            result.append([nums1[i],nums2[j]])
            

            if j < len(nums2) - 1:
                heappush(min_heap,(nums1[i] + nums2[j + 1], i, j + 1) )
                # print("pushed: ",min_heap)

        

        return result