import heapq

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # max_heap = [ -i for i in a]
    # heapq.heapify(max_heap)

    # mx = -heapq.heappop(max_heap)
    # next_mx = -heapq.heappop(max_heap)

    # print (next_mx - 1)
    # # mx = max(a)
    # # print(mx - 1)

    mx_k = -float('inf')
    mn = a[0]

    heap = []
    heapq.heappush(heap, a[0])

    window = 1

    for i in range(1, n):
        heapq.heappush(heap, a[i])
        mn = min(mn, heap[0])

        if len(heap) > window:
            heapq.heappush(heap)
        window += 1

        if mn < mx_k:
            mx_k = mn
    
    print(mx_k)
