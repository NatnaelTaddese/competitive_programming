class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        # curr = 0
        # # if we sort, we need to keep track of the indexes
        # tasks = sorted(tasks)

        # for i, enq, procc in tasks:
             
        # while min_heap:

        indexed_tasks = [(enqueue, processing, i) for i, (enqueue, processing) in enumerate(tasks)]
        indexed_tasks.sort()

        min_heap = []
        result = []
        time = 0
        i = 0
        n = len(tasks)
        
        
        while i < n or min_heap:
            if not min_heap and i < n and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]
            
            while i < n and indexed_tasks[i][0] <= time:
                enqueue, processing, index = indexed_tasks[i]
                heapq.heappush(min_heap, (processing, index))
                i += 1
            
            if min_heap:
                processing, index = heapq.heappop(min_heap)
                time += processing
                result.append(index)
        
        return result