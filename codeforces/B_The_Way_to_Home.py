from collections import deque


n, d = map(int, input().split())
# a = list(map(int, input().split()))

a = list(input())

queue = deque([(0)])

#  track the minimal jump
jumps = [float('inf') for _ in range(n)] 
jumps[0] = 0

while queue:
    current = queue.popleft()
        
    
    for jump in range(1, d + 1):
        next_point = current + jump
        
        
        if next_point < n and a[next_point] == '1':
            # If not visited
            if jumps[next_point] == float('inf'):  
                jumps[next_point] = jumps[current] + 1
                queue.append(next_point)
                
                if next_point == n - 1:
                    print(jumps[next_point])
                    exit()


print(-1)