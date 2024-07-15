from collections import defaultdict
 
 
for _ in range(int(input())):
    n, m = map(int, input().split())
 
    edges = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int,input().split())
 
        edges[u].append(v)
        edges[v].append(u)
    
 
    answer = []
    x,y = 0 , 0
 
 
    primary = False
 
    # print(edges)
 
    for vertex in edges:
        if len(edges[vertex]) == 1:
            continue
        if len(edges[vertex]) in answer and len(edges[vertex]) == answer[0]:
            primary = True
            
        else:
            answer.append(len(edges[vertex]))
    
    if len(answer) == 1:
        answer.append(answer[0])
        # answer.reverse()
    if primary:
        print(answer[1], answer[0] - 1)
 
    else:
        print(answer[0], answer[1] - 1)