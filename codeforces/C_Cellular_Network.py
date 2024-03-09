n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

distance = 0

tower = 0

for city in a:
     ####
    for i in range(tower, len(b) - 1):
        # find the smallest distance
        
        if (b[i] < b[i + 1]):
            break
        else:
            tower = i
    
    distance = max(distance, b[tower] - a[i])
    


print(distance)
