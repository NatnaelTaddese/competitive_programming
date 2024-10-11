class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # to make this a max heap(max always on top to pop)
        # we negate the key
        heap = [(-value, key) for key, value in count.items()]
        
        heapify(heap)

        result = []

        for _ in range(k):
            key, val = heappop(heap)
            result.append(val)

        return result
        