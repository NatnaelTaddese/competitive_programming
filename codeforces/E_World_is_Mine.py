'''
[1,2,3,4]
alice: 4 2
bob: 3 1

2 6 5 3 9 1 6 2 5 6 3 2 3 9 6 1 6

[1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 6, 6, 6, 6, 6, 9, 9]

1 2 3
9 9 6

[1,2,3,5,6,9]



alice:9 6 5 3 2
[3, 5, 6, 6, 6, 6, 9]
alc:2_ 3_ 5_ 6_ 9_
bob:1_ 1_ 2_ 2_ 3_

'''
# print(sorted(list(map(int, "2 6 5 3 9 1 6 2 5 6 3 2 3 9 6 1 6".split() ))))
import heapq
from collections import Counter

for _ in range(int(input())):

    n = int(input())
    cakes = list(map(int, input().split()))
    # cakes.sort()
    # to_eat = Counter(cakes)

    # a_wants = sorted(set(cakes))
    # a_eats = 0
    # a_eaten = set()
    # alice_turn = True

    # a_i = 0
    # while a_i < len(a_wants) and len(to_eat) > 0:
    #     if alice_turn:
    #         while a_i < len(a_wants):
    #             if a_wants[a_i] in to_eat:
    #                 a_eats += 1
    #                 #debug
    #                 # print("Alice ate: ",a_wants[a_i] )
    #                 a_eaten.add(a_wants[a_i])
    #                 to_eat[a_wants[a_i]] -= 1

    #                 if to_eat[a_wants[a_i]] == 0:
    #                     del to_eat[a_wants[a_i]]

    #                 a_i += 1
    #                 break
    #             a_i += 1

    #         alice_turn = not alice_turn

    #     else:
    #         # cake = max(to_eat)
    #         # to_eat[cake] -= 1
    #         # if to_eat[cake] == 0:
    #         #     del to_eat[cake]
    #         # alice_turn = not alice_turn
    #         sorted_cakes = sorted(to_eat.items(), key=lambda y: y[1])
    #         for cake in  sorted_cakes:
    #             if cake[0] in a_eaten:
    #                 continue
    #             to_eat[cake[0]] -= 1
    #             #debug
    #             print("Bob eats: ", cake[0])
    #             if to_eat[cake[0]] == 0:
    #                 del to_eat[cake[0]]
    #             break
    #         alice_turn = not alice_turn

    remaining_rounds = 1
    eaten = 0

    heap = []

    freq = sorted([[key,val] for key, val in Counter(cakes).items()])


    for i in range(1,len(freq)):
        if freq[i][1] > remaining_rounds:
            if heap and -heap[0] > freq[i][1]:
                    remaining_rounds -= heapq.heappop(heap) + freq[i][1]
                    heapq.heappush(heap, -freq[i][1])
                
            remaining_rounds += 1
        else:
            eaten += 1
            remaining_rounds -= freq[i][1]
            heapq.heappush(heap, -freq[i][1])

    print(len(freq) - eaten)

    # print(a_eats)
