from heapq import heappop, heappush


n = int(input())
a = list(map(int, input().split()))

total = 0
health = 0
mx_count = 0

heap = []

# for potion in a:
#     if health + potion >= 0:
#         print(potion)
#         health += potion
#         total += 1

# print(total)

# def backtrack(index, health, count):
#     global mx_count
#     if index == len(a):
#         mx_count = max(mx_count, count)
#         return
    
#     #skip
#     backtrack(index + 1, health, count)

#     #if no skip
#     if health + a[index] >= 0:
#         backtrack(index + 1, health + a[index], count + 1)

for potion in a:
    if health + potion >= 0:
        health += potion
        heappush(heap,potion)
        mx_count += 1
        
    else:
        if heap:
            if heap[0] < potion:
                health += potion
                health -= heappop(heap)
                
                heappush(heap,potion)


# backtrack(0,0,0)
print(mx_count)

