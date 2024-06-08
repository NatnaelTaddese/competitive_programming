n = int(input())

angels = []

for _ in range(n):
    angels.append(int(input()))


def backtrack(index, curr):
    if index == n:
        return curr % 360 == 0
    
    # clockwise
    if backtrack(index + 1, curr + angels[index]):
        return True
    
    if backtrack(index + 1, curr - angels[index]):
        return True
    
    # forgot my default case
    return False
    

if backtrack(0,0):
    print("YES")
else:
    print("NO")

