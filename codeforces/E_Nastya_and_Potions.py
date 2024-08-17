"""
has: (1)items -> 3

30 8 3 5 10

3: 2 4 5 = 8 + 5 + 10 
0:       = 8
0:       = 3 (had)
2: 3 5   = 3 (had) + 10
0:       = 10

"""

from collections import defaultdict


for _ in range(int(input())):
    n, k = map(int, input().split())

    graph = defaultdict(list)

    c = list(map(int,input().split()))

    unlimited = set(list(map(int,input().split())))

    for i in range(n):
        m = list(map(int,input().split()))
        if len(m) == 1:
            graph[c[i]]
        else:
            graph[c[i]].extend(m[1:])
    
    # print(graph)


    roots = []
    for key, value in graph.items():
        if len(value) == 0 and key not in unlimited:
            roots.append(key)
            unlimited.add(key)
            total += key
    
    for price in c:
        total = 0

        value = graph[price]

        if len(value) > 1:
            for i in value:
                if c[i - 1] not in unlimited:
                    total += c[i - 1]
                    unlimited.add(key)

    # for key, value in graph.items():
        if len(value) > 1:
            for i in value:
                if c[i - 1] not in unlimited:
                    total += c[i - 1]
                    unlimited.add(key)

    print(total)




    

    
