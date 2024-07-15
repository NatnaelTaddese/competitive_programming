class MedianFinder(object):

    def __init__(self):
        # self.heap = []
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # heapq.heappush(self.heap, num)
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
           heappush(self.min_heap, num)

        # but ofc we have to balance the two heaps....
        if len(self.max_heap) > len(self.min_heap) + 1:
            temp = -heappop(self.max_heap)
            heappush(self.min_heap, temp)

        elif len(self.min_heap) > len(self.max_heap):
            temp = -heappop(self.min_heap)
            heappush(self.max_heap, temp)


    def findMedian(self):
        """
        :rtype: float
        """
        # return self.heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()