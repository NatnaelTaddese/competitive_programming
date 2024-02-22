def isSubset( a1, a2, n, m):
    
    if m > n:
        return "No"
    
    seen = dict()
    for element in a1:
        seen[element] = seen.get(element, 0) + 1
    
    for element in a2:
        if element not in seen:
            return "No"
            break
        if seen.get(element, 0) == 0:
            return "No"
            break
        seen[element] -= 1
        
    return "Yes"
        
    
    
    
