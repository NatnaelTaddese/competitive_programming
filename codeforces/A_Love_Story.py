def split(word): 
    return [char for char in word]  

c = "codeforces"
c = split(c)

for _ in range(int(input())):
    n = input()
    n = split(n)

    left = 0
    right = len(n) - 1

    result = 0
    while(left <= right):
        if c[left] != n[left]:
            result += 1
        if c[right] != n[right]:
            result += 1
        
        left += 1
        right -= 1  
    
    print(result)
