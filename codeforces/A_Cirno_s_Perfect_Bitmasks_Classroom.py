for _ in range(int(input())):
    x = int(input())


    y1 = 1
    while (x & y1) == 0:
        y1 <<= 1  

    y2 = 1
    while (x ^ y2) == 0:
        y2 <<= 1  
    
    candidates = [y1 | y2]
    if (x & y1) != 0 and (x ^ y1) != 0: 
        candidates.append(y1)
    if (x & y2) != 0 and (x ^ y2) != 0:
        candidates.append(y2)
    
    
    print (min(candidates))