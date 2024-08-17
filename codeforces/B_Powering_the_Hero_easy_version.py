from heapq import heappop, heappush


for _ in range(int(input())):
    n = int(input())
    cards = list(map(int, input().split()))

    max_heap = []

    total = 0

    for card in cards:
        if card > 0:
            heappush(max_heap, -card)
        
        else:
            if max_heap:
                total += -heappop(max_heap)
    
    print(total)