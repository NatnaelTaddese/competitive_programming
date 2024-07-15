class Solution(object):

    # def heapify(self,arr, n, i):
    #         parent = i
    #         left = 2*i + 1
    #         right = 2*i + 2
            
    #         if left < n and arr[left] > arr[parent]:
    #             parent = left
    #         if right < n and arr[right] > arr[parent]:
    #             parent = right
                
    #         if parent != i:
    #             arr[i], arr[parent] = arr[parent], arr[i]
    #             self.heapify(arr, n, parent)
                

    # def buildHeap(self,arr,n):
    #         start = n // 2 - 1
            
    #         for i in range(start, -1, -1):
    #             self.heapify(arr,n,i)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        # n = len(nums)
        # self.buildHeap(nums, n)
        
        # for i in range(n-1, k - 2, -1):
        #     nums[i], nums[0] = nums[0], nums[i]
            
        #     self.heapify(nums,i,0)
        
        # return nums[n - k]
        heap = []

        for num in nums:
            heappush(heap, num)

            if len(heap) > k:
                heappop(heap)
        
        return heap[0]
    
        